# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160413_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='diagFour_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'diagnosis 4 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='diagOne_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'diagnosis 1 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='diagThree_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'diagnosis 3 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='diagTwo_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'diagnosis 2 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medFive_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Medicine 5 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medFour_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Medicine 4 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medOne_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Medicine 1 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medThree_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Medicine 3 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medTwo_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Medicine 2 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='procedureOne_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Procedure 1 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='procedureThree_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Procedure 3 Date', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='procedureTwo_date',
            field=models.DateField(max_length=255, null=True, verbose_name=b'Procedure 2 Date', blank=True),
        ),
    ]
