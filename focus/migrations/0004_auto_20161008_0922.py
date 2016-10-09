# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0003_auto_20161008_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='task',
            field=models.TextField(verbose_name=b'task'),
        ),
    ]
