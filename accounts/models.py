from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Usermanager(BaseUserManager):
    def create_user(self,email,password=None,is_staff=False,is_admin=False,is_active=True):
        if not email:
            raise ValueError('Users must have an email.')
        if not password:
            raise ValueError('Users must have a password')
        user_obj=self.model(
        email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.active=is_active
        user_obj.save(using=self._db)
        return user_obj
    def create_staffuser(self,email,password=None):
        user=self.create_user(
        email,
        password=password,
        is_staff=True

        )
        return user
    def create_superuser(self,email,password=None):
        user=self.create_user(
        email,
        password=password,
        is_staff=True,
        is_admin=True
        )

class User(AbstractBaseUser):
    email=models.EmailField(max_length=250,unique=True,default='@gmail.com')
    full_name=models.CharField(max_length=250,blank=True,null=True)
    active=models.BooleanField(default=True)
    admin=models.BooleanField(default=False)
    staff=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=Usermanager()
    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
