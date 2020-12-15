from django.contrib import admin

# Register your models here.

from .models import *

class RoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')

class ForfaitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'hours_paid')

class RdvAdmin(admin.ModelAdmin):
    list_display = ('user', 'hours', 'date', 'places', 'instructor')

admin.site.register(Forfait, ForfaitAdmin)
admin.site.register(Rdv, RdvAdmin)
admin.site.register(Role, RoleAdmin)


