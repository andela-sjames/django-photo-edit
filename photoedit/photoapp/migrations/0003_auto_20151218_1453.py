# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import photoapp.models
import photoapp.filesizechecker


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0002_auto_20151215_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photoapp.filesizechecker.LimitImageField(upload_to=photoapp.models.get_upload_file_name, blank=True),
        ),
    ]
