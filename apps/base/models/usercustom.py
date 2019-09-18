# -*- coding: utf-8

import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from ..rename_image import RenameImage


def image_path(instance, filename):
    return os.path.join('avatar', str(instance.pk) + '.' + filename.rsplit('.', 1)[1])

    
class PyUser(AbstractUser):
    ''' User Model '''
    SEXO_CHOICES = (
        ('F', _('FEMALE')),
        ('M', _('MALE')),
    )

    password = models.CharField(_("Password"), max_length=128)
    last_login = models.DateTimeField(_("Last login"), default=timezone.now)
    is_superuser = models.BooleanField(_("Super Admin"), default=False, db_index=True)
    is_staff = models.BooleanField(_("Staff"), default=False, db_index=True)
    is_active = models.BooleanField(_("Active"), default=False)
    username = models.CharField(_("User name"), max_length=150, db_index=True, unique=True)
    first_name = models.CharField(_("Name"), max_length=30)
    last_name = models.CharField(_("Last name"), max_length=30)
    email = models.CharField(_("Email"), max_length=254, null=False, db_index=True, unique=True)
    telefono = models.CharField(_("Phone"), max_length=255, blank=True, null=True)
    celular = models.CharField(_("Mobile Phone"), max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(_("Birthdate"), blank=True, null=True)
    sexo = models.CharField(_("Sex"), max_length=255, choices=SEXO_CHOICES, blank=True, null=True)
    avatar = models.ImageField(max_length=255, storage=RenameImage(), upload_to=image_path, blank=True, null=True, default='avatar/default_avatar.png')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        db_table = 'auth_user'
