# Generated by Django 4.2.6 on 2024-06-18 14:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('body', models.TextField(verbose_name='Matni')),
                ('photo', models.ImageField(upload_to='blogs/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])], verbose_name='Rasmi')),
                ('video', models.FileField(blank=True, null=True, upload_to='blogs/videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Videosi')),
                ('slug', models.SlugField(verbose_name='Manzil')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': 'Maqolalar',
                'db_table': 'blogs',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': "Bo'lim",
                'verbose_name_plural': "Bo'limlar",
                'db_table': 'categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Izoh',
                'verbose_name_plural': 'Izohlar',
                'db_table': 'comments',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Layk',
                'verbose_name_plural': 'Layklar',
                'db_table': 'likes',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Teg',
                'verbose_name_plural': 'Teglar',
                'db_table': 'tags',
                'ordering': ['-id'],
            },
        ),
    ]
