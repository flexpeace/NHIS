# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160412_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='medQTYTwo',
            field=models.IntegerField(default=0, verbose_name=b'Medicine 2 Quantity', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medQTYone',
            field=models.IntegerField(default=0, verbose_name=b'Medicine 1 Quantity', blank=True),
        ),
    ]
