# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0004_auto_20161008_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='stat',
            field=models.TextField(default=b'', max_length=256, verbose_name=b'stat'),
        ),
    ]
