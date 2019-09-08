from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.



class UserProfileManager(BaseUserManager):
    """WORK WITH CUSTOME USER MODEL"""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        # normalize emails as all uppercase or lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # to make hashed password
        user.set_password(password)
        # save in same db created
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name , password):
        """Creates  user profile object with password."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser ,PermissionsMixin):
    """PRESENT USER PROFILE"""
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

# user's fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']      #check for the spilling

# help functions

    # used by django admin
    def get_full_name(self):
        return self.name

    # ex : get first name only
    def get_short_name(self):
        return self.name


    #used to convert the object to string
    def __str__(self):
        return self.email              # because email is unique


##### note : to make superuser writr :   python manage.py createsuperuser #####









