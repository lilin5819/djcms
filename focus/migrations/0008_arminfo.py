# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0007_auto_20161008_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camera_state', models.BooleanField(default=False, verbose_name=b'camera_state')),
                ('light', models.IntegerField(default=0, verbose_name=b'light_strength')),
                ('humidity', models.IntegerField(default=0, verbose_name=b'humidity')),
                ('temperature', models.IntegerField(default=0, verbose_name=b'temperature')),
            ],
        ),
    ]
