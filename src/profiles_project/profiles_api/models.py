from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """ work with a custum user manager"""

    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """ Create  """


        user = self.create_suer(email, name, password)

        user.is_superuser = True
        user.is_staff = True


        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents a "user profile" in our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    if_staff = models.BooleanField(default=True)

    objets = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get users full name"""
        return self.name


    def get_short_name(self):
        """used to get users short name"""
        return self.name


    def __str__(self):
        """ For converting the object to a string"""
        return self.email
