from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Provincia(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Distrito(models.Model):
    """Model definition for District."""

    # TODO: Define fields here
    name = models.CharField(max_length=100)
    provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)
   
    def __str__(self):
        """Unicode representation of District."""
        return self.name

class UnidadeSanitaria(models.Model):
    """Model definition for HealthFacility."""
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    # openmrs_name = models.CharField(max_length=255, null=True, blank=True)
    distrito = models.ForeignKey('Distrito', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for HealthFacility."""

        verbose_name = 'Unidade Sanitaria'
        verbose_name_plural = 'Unidades Sanitarias'

    def __str__(self):
        """Unicode representation of HealthFacility."""
        return self.name

class Livro(models.Model):
    tipo = models.CharField(max_length=100)
    numero = models.IntegerField()
    pagina = models.IntegerField()  
    linha = models.IntegerField()
    
    def __str__(self):
        return f'{self.tipo} {self.numero}'
    
    