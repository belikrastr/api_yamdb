from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


ROLES = [('user', ' user'),
         ('moderator', 'модер'),
         ('admin', 'админ')
         ]


class User(AbstractUser):
    """модель пользователя c приколами"""

    username = models.CharField(blank=False, null=False,
                                unique=True, max_length=25,
                                validators=[UnicodeUsernameValidator])

    first_name = models.CharField(null=False,   blank=True, max_length=25)

    last_name = models.CharField(null=False, blank=True, max_length=25)

    email = models.EmailField(blank=False, null=False, unique=True,
                              max_length=50)

    bio = models.TextField(blank=True, null=True, max_length=100)

    role = models.CharField(choices=ROLES, max_length=25, default='user')

    confirmation_code = models.CharField(max_length=100, blank=True, null=True)

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'

    def __str__(self):
        return self.username