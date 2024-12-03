from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('account:redactor-list', kwargs={'pk': self.pk})