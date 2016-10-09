# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='stat',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'stat'),
        ),
        migrations.AddField(
            model_name='author',
            name='task',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'task'),
        ),
        migrations.AlterField(
            model_name='author',
            name='password',
            field=models.CharField(default=b'123', max_length=256, verbose_name=b'password'),
        ),
    ]
