from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    email = models.EmailField('E-Mail', unique=True)
    phone = models.CharField('Celular', max_length=20, null=True, blank=True)
    # image = models.ImageField('Imagem', upload_to='accounts/images', default='accounts/images/user_default_photo.png')  # , null=True, blank=True
    created_date_at = models.DateTimeField('Registrado em', auto_now_add=True)
    updated_date_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return None

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
