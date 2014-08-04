from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, email, name=None, password=None):
		if not email:
			raise valueError('Users must have e-mail address')

		user = self.model(
			email=self.normalize_email(email),
			name=name
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, name=None):
		user = self.create_user(email, name, password=password)
		user.is_active = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	email = models.EmailField(max_length=100, unique=True)
	name = models.CharField(max_length=255, null=True, default='')
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	objects = UserManager()

	USERNAME_FIELD = 'email'

	def get_full_name(self):
		return self.name if self.name else self.email

	def get_short_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	def __unicode__(self):
		return self.email

	@property
	def is_staff(self):
		return self.is_superuser