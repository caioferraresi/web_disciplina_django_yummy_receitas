from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    username = models.CharField(_('username'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.name

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.name