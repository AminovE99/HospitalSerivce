# Generated by Django 4.0.3 on 2022-03-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='diagnoses',
            field=models.ManyToManyField(to='patient.diagnosis', verbose_name='Диагнозы'),
        ),
    ]
