from django.db import models
from rest_framework.authtoken.models import Token


class Patient(models.Model):
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    diagnoses = models.ManyToManyField('Diagnosis', verbose_name='Диагнозы')


class Diagnosis(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False, verbose_name="Название диагноза")
    description = models.CharField(max_length=256, null=True, blank=True, verbose_name="Описание диагноза")

    def __str__(self):
        return self.title


class CustomToken(Token):
    is_doctor = models.BooleanField(default=False)
