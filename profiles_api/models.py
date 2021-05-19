from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("user must have user adress")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)#saves in every database that the project is connected#
        
        return user

    def create_superuser(self,email,name,password):
        """create and save a new superuser using given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def getFullName(self):
        """Retrive full name of user"""
        return self.name

    def getShortName(self):
        """Retrive short name of user"""
        return self.name 

    def __str__(self):
        """Return string representation of our user"""
        return self.email