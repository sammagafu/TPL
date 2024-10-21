# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    favorite_team = models.ForeignKey(
        'teams.Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='favourite_team'
    )
    notifications_enabled = models.BooleanField(default=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="user",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.username
