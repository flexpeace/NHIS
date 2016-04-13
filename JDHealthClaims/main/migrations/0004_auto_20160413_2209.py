# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160413_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='first_visit_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'First Visit Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='forth_visit_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Fourth Visit Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='second_visit_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Second Visit Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='third_visit_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Third Visit Date', blank=True),
        ),
    ]
