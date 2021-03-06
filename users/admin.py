from __future__ import absolute_import

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('email', 'name', ' is_superuser')
	list_filter = ('is_superuser')

	fieldsets = {
	(None, {
		'fields': ('email', 'name', 'password', 'is_superuser', 'is_active'
		)}),
		('Groups', {'fields': ('groups',)})
)

	add_fieldsets = {
	(None, {
		'classes': ('wide',),
		'fields': ('email', 'name', 'password1', 'password2')}
		),
	)

	search_fields = ('email', 'name')
	ordering = ('email',)
	filter_horizontal = ('groups',)

admin.site.register(User, CustomUserAdmin)