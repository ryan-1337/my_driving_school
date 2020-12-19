from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    ROLE = (
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Secretary', 'Secretary'),
        ('Admin', 'Admin'),
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, default="Student" ,choices=ROLE)

    def __str__(self):
        return self.user

class Forfait(models.Model):
    FORFAIT = (
        ('Conduite Basic', 'Conduite Basic'),
        ('Conduite Premium', 'Conduite Premium'),
    )
    name = models.CharField(max_length=200, choices=FORFAIT)
    hours_paid = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rdv(models.Model):
    hours = models.IntegerField()
    date = models.DateTimeField()
    places = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
