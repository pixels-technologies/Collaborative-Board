from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        '''
        Creates and saves a User with the given email and password.
        '''
        
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError("The password must be set")
        
        # normalize_email() keeps the entered email in lower cases
        email = self.normalize_email(email)
        
        # self.model equates to User() class
        user = self.model(email=email, **extra_fields)
        
        # Contains Hash logic for the password
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        '''
        Creates and saves a superuser with the given email and password.
        '''
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom User model that uses email as the unique identifier instead of username.
    '''
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Assign the custom UserManager
    objects = CustomUserManager()
    
    '''
    The USERNAME_FIELD attribute specifies the field in your model that will be used
    as the unique identifier for the user. By default, Django uses the username
    '''
    USERNAME_FIELD = 'email'
    
    '''
    The REQUIRED_FIELDS attribute specifies a list of fields that must be provided when using
    the createsuperuser management command or when creating a user programmatically.
    These fields are in addition to the USERNAME_FIELD, which is always required.
    '''
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        '''
        Return a string representation of the user's email
        '''
        
        return self.email
