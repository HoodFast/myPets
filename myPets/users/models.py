
from collections import namedtuple
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

ROLES_NAME = namedtuple('ROLES_NAME', 'user admin')
ROLES = ROLES_NAME('user', 'admin')
ROLE_CHOICES = (
    ('user', ROLES.user),
    ('admin', ROLES.admin),
)
class CastomUser(AbstractUser):
    """Castom model user."""
    role = models.CharField(
        verbose_name='Роль пользователя',
        choices=ROLE_CHOICES,
        default=ROLES.user,
        max_length=max(len(role) for _, role in ROLE_CHOICES),
    )
    first_name = models.CharField(max_length=150, blank=True)
    
    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def is_admin(self):
        return self.role == ROLES.admin

    def __str__(self):

        return self.username[:30]
    
    def save(self,*args,**kwargs):
        created = not self.pk
        super().save(*args,**kwargs)
        if created:
            Profile.objects.create(user=self, id=self.id)

class Profile(models.Model):
    user = models.OneToOneField(to='CastomUser', null=True , on_delete=models.CASCADE)
    first_name = models.CharField('Имя пользователя',max_length=30,blank=True)
    last_name = models.CharField('Фамилия пользователя',max_length=30,blank=True)
    city = models.CharField('город',max_length=30,blank=True)
    phone_number = PhoneNumberField(blank=True)
    status = models.TextField(blank=True)
