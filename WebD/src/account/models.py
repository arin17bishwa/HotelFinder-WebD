from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('EMAIL ID IS REQUIRED')
        if not username:
            raise ValueError('USERNAME IS REQUIRED')

        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email               = models.EmailField(max_length=254,unique=True,verbose_name='Email ID',blank=False)
    username            = models.CharField(max_length=20,unique=True,blank=False,verbose_name='Username')
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email']

    objects=MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,object=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
