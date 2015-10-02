# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20151002_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='send_push_notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='send_push_notification',
            field=models.BooleanField(default=False),
        ),
    ]
