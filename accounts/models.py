from django.contrib.auth.models import AbstractUser
from django.db import models

TYPE = (('Employer', 'Employer'), ('Applicant', 'Applicant'))


class Account(AbstractUser):
    type = models.CharField(max_length=1000, null=False, verbose_name='Name', choices=TYPE)
    email = models.EmailField(verbose_name='Email', unique=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
