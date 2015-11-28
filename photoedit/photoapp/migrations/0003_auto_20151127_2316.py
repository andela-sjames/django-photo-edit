# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoapp', '0002_auto_20151127_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('image', cloudinary.models.CloudinaryField(default=b'img/photo_default.png', max_length=255, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('tags', models.ManyToManyField(to='photoapp.Tag', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
