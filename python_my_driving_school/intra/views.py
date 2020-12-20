from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import UpdateView

from .forms import CreateUserForm, ChangeUserForm
from .decorators import unauthenticated_user, allowed_users
from .models import User, Forfait, Rdv


# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.user.groups.all()[0] == Group.objects.get(name='student'):
        forfait = Forfait.objects.filter(user_id=request.user.pk)[0]
        hoursPaid = forfait.hours_paid
        subscribeDate = forfait.date_created

        allRdv = Rdv.objects.filter(user_id=request.user.pk).all()

        context = {'forfait': forfait, 'hoursPaid': hoursPaid, 
        'subscribeDate': subscribeDate, 'allRdv': allRdv} 
        return render(request, 'accounts/dashboard.html', context)
    elif request.user.groups.all()[0] == Group.objects.get(name='instructor'):

        allRdv = Rdv.objects.filter(instructor=request.user.username).all()

        context = {'allRdv': allRdv} 
        return render(request, 'accounts/dashboard.html', context)
    else: 
        return render(request, 'accounts/dashboard.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'secretary'])
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)

            messages.success(request, 'Compte créer: ' + username)

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(
                request, 'Nom d\'utilisateur ou mot de passe incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def editProfil(request):
    form = ChangeUserForm()

    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, 'Compte mit à jour')

    context = {'form': form}
    return render(request, 'accounts/edit_profil.html', context)
