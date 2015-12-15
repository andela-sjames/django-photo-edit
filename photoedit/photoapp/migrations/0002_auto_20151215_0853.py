# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import photoapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=photoapp.models.get_upload_file_name, blank=True),
        ),
    ]
