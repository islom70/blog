# Generated by Django 4.2.6 on 2024-06-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birthday',
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Erkak'), ('female', 'Ayol')], max_length=10, null=True, verbose_name='Jinsi'),
        ),
    ]
