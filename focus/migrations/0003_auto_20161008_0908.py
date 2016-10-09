# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0002_auto_20161008_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='task',
            field=models.TextField(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1'),
        ),
    ]
