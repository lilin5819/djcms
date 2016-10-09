# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0008_arminfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='taskcolor',
            field=models.CharField(default=b'default', max_length=256, verbose_name=b'taskcolor'),
        ),
        migrations.AddField(
            model_name='author',
            name='taskprogress',
            field=models.IntegerField(default=0, verbose_name=b'taskprogress'),
        ),
    ]
