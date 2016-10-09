# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0006_auto_20161008_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='author',
            name='stat',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'stat'),
        ),
    ]
