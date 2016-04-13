# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20160413_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='owner',
            field=models.ForeignKey(verbose_name=b'user', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='ClaimNumber',
            field=models.CharField(max_length=255, verbose_name=b'Claim Number', blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='GDRGOneprocedure',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'G-DRG Procedure 1', choices=[(b'', b'--Procedure Description--'), (b'None', b'None')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='GDRGThreeprocedure',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'G-DRG Procedure 3', choices=[(b'', b'--Procedure Description--'), (b'None', b'None')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='GDRGTwoprocedure',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'G-DRG Procedure 2', choices=[(b'', b'--Procedure Description--'), (b'None', b'None')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='attendance',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Type of Attendance', choices=[(b'', b'--Attendance--'), (b'Chronic Follow-Up', b'Chronic Follow-Up'), (b'Emgergency/Acute episode', b'Emgergency/Acute episode')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medFiveDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Medicine 5 Description', choices=[(b'', b'--Medicine Code--'), (b'ACETAZIN1', b'ACETAZIN1'), (b'ACETAZTA1', b'ACETAZTA1'), (b'ACETYLIN1', b'ACETYLIN1'), (b'ACETYLTA1', b'ACETYLTA1'), (b'ACETYLDT1', b'ACETYLDT1'), (b'ACTCHAPO1', b'ACTCHAPO1'), (b'ACICLOCR1', b'ACICLOCR1'), (b'ACICLOEO1', b'ACICLOEO1'), (b'ACICLOIN1', b'ACICLOIN1'), (b'ACICLOSU2', b'ACICLOSU2'), (b'ACICLOTA1', b'ACICLOTA1'), (b'ADRENAIN1', b'ADRENAIN1'), (b'ADRENAIN2', b'ADRENAIN2'), (b'ADRIAMIN1', b'ADRIAMIN1'), (b'ALBENDTA1', b'ALBENDTA1'), (b'ALBENDTA2', b'ALBENDTA2'), (b'ALLOPUTA1', b'ALLOPUTA1'), (b'ALLOPUTA2', b'ALLOPUTA2'), (b'AMIACIIN1', b'AMIACIIN1')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medFourDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Medicine 4 Description', choices=[(b'', b'--Medicine Code--'), (b'ACETAZIN1', b'ACETAZIN1'), (b'ACETAZTA1', b'ACETAZTA1'), (b'ACETYLIN1', b'ACETYLIN1'), (b'ACETYLTA1', b'ACETYLTA1'), (b'ACETYLDT1', b'ACETYLDT1'), (b'ACTCHAPO1', b'ACTCHAPO1'), (b'ACICLOCR1', b'ACICLOCR1'), (b'ACICLOEO1', b'ACICLOEO1'), (b'ACICLOIN1', b'ACICLOIN1'), (b'ACICLOSU2', b'ACICLOSU2'), (b'ACICLOTA1', b'ACICLOTA1'), (b'ADRENAIN1', b'ADRENAIN1'), (b'ADRENAIN2', b'ADRENAIN2'), (b'ADRIAMIN1', b'ADRIAMIN1'), (b'ALBENDTA1', b'ALBENDTA1'), (b'ALBENDTA2', b'ALBENDTA2'), (b'ALLOPUTA1', b'ALLOPUTA1'), (b'ALLOPUTA2', b'ALLOPUTA2'), (b'AMIACIIN1', b'AMIACIIN1')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medOneDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Medicine 1 Description', choices=[(b'', b'--Medicine Code--'), (b'ACETAZIN1', b'ACETAZIN1'), (b'ACETAZTA1', b'ACETAZTA1'), (b'ACETYLIN1', b'ACETYLIN1'), (b'ACETYLTA1', b'ACETYLTA1'), (b'ACETYLDT1', b'ACETYLDT1'), (b'ACTCHAPO1', b'ACTCHAPO1'), (b'ACICLOCR1', b'ACICLOCR1'), (b'ACICLOEO1', b'ACICLOEO1'), (b'ACICLOIN1', b'ACICLOIN1'), (b'ACICLOSU2', b'ACICLOSU2'), (b'ACICLOTA1', b'ACICLOTA1'), (b'ADRENAIN1', b'ADRENAIN1'), (b'ADRENAIN2', b'ADRENAIN2'), (b'ADRIAMIN1', b'ADRIAMIN1'), (b'ALBENDTA1', b'ALBENDTA1'), (b'ALBENDTA2', b'ALBENDTA2'), (b'ALLOPUTA1', b'ALLOPUTA1'), (b'ALLOPUTA2', b'ALLOPUTA2'), (b'AMIACIIN1', b'AMIACIIN1')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medThreeDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Medicine 3 Description', choices=[(b'', b'--Medicine Code--'), (b'ACETAZIN1', b'ACETAZIN1'), (b'ACETAZTA1', b'ACETAZTA1'), (b'ACETYLIN1', b'ACETYLIN1'), (b'ACETYLTA1', b'ACETYLTA1'), (b'ACETYLDT1', b'ACETYLDT1'), (b'ACTCHAPO1', b'ACTCHAPO1'), (b'ACICLOCR1', b'ACICLOCR1'), (b'ACICLOEO1', b'ACICLOEO1'), (b'ACICLOIN1', b'ACICLOIN1'), (b'ACICLOSU2', b'ACICLOSU2'), (b'ACICLOTA1', b'ACICLOTA1'), (b'ADRENAIN1', b'ADRENAIN1'), (b'ADRENAIN2', b'ADRENAIN2'), (b'ADRIAMIN1', b'ADRIAMIN1'), (b'ALBENDTA1', b'ALBENDTA1'), (b'ALBENDTA2', b'ALBENDTA2'), (b'ALLOPUTA1', b'ALLOPUTA1'), (b'ALLOPUTA2', b'ALLOPUTA2'), (b'AMIACIIN1', b'AMIACIIN1')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='medTwoDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Medicine 2 Description', choices=[(b'', b'--Medicine Code--'), (b'ACETAZIN1', b'ACETAZIN1'), (b'ACETAZTA1', b'ACETAZTA1'), (b'ACETYLIN1', b'ACETYLIN1'), (b'ACETYLTA1', b'ACETYLTA1'), (b'ACETYLDT1', b'ACETYLDT1'), (b'ACTCHAPO1', b'ACTCHAPO1'), (b'ACICLOCR1', b'ACICLOCR1'), (b'ACICLOEO1', b'ACICLOEO1'), (b'ACICLOIN1', b'ACICLOIN1'), (b'ACICLOSU2', b'ACICLOSU2'), (b'ACICLOTA1', b'ACICLOTA1'), (b'ADRENAIN1', b'ADRENAIN1'), (b'ADRENAIN2', b'ADRENAIN2'), (b'ADRIAMIN1', b'ADRIAMIN1'), (b'ALBENDTA1', b'ALBENDTA1'), (b'ALBENDTA2', b'ALBENDTA2'), (b'ALLOPUTA1', b'ALLOPUTA1'), (b'ALLOPUTA2', b'ALLOPUTA2'), (b'AMIACIIN1', b'AMIACIIN1')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='outcome',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Outcome', choices=[(b'', b'--Outcome--'), (b'Discharged', b'Discharged'), (b'Died', b'Died'), (b'Transferred Out', b'Transferred Out'), (b'Absconded', b'Absconded')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='procedureOneDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Precedure 1 Description', choices=[(b'', b'--Procedure Description--'), (b'None', b'None')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='procedureThreeDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Precedure 3 Description', choices=[(b'', b'--Procedure Description--'), (b'None', b'None')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='procedureTwoDescription',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Precedure 2 Description', choices=[(b'', b'--Procedure Description--'), (b'None', b'None')]),
        ),
        migrations.AlterField(
            model_name='claim',
            name='typeOfService',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Type of service (i)', choices=[(b'', b'--Service--'), (b'Outpatient', b'Outpatient'), (b'Diagnostic', b'Diagnostic'), (b'In-Patient', b'In-Patient'), (b'All Inclusive', b'All Inclusive'), (b'Unbundled', b'Unbundled')]),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='level',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Level of prescribing', choices=[(b'', b'---Level of health care provided--'), (b'A', b'Chips compound'), (b'B1', b'Health Centre without a Doctor'), (b'B2', b'Health centre with a Doctor'), (b'M', b'Maternity home with Midwife'), (b'C', b'District Hospital'), (b'D', b'Regional Hospital'), (b'E', b'Teaching Hospital')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(default=18, verbose_name=b'Age', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'Gender', choices=[(b'', b'--Gender--'), (b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='level',
            field=models.CharField(max_length=255, verbose_name=b'Provider Type', choices=[(b'', b'---Level of health care provided--'), (b'A', b'Chips compound'), (b'B1', b'Health Centre without a Doctor'), (b'B2', b'Health centre with a Doctor'), (b'M', b'Maternity home with Midwife'), (b'C', b'District Hospital'), (b'D', b'Regional Hospital'), (b'E', b'Teaching Hospital')]),
        ),
    ]
