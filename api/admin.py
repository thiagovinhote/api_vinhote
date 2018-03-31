from django.contrib import admin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import *
from .models import *

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('avatar', 'username', 'first_name', 'last_name',)}),
        ('Profile', {'fields': ('role', 'bio',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       )}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)

admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Link)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Certificate)
