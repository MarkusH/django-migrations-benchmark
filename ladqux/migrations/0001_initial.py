# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0001_initial'),
        ('etnevwmkj', '0002_wpkevitz_eqzsll'),
        ('ftcfrcnas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oeyhu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yzqcicylut', models.ForeignKey(null=True, related_name='+', to='etnevwmkj.Lsmxy')),
            ],
        ),
        migrations.CreateModel(
            name='Yfyadqk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dljxy', models.CharField(default='', max_length=176)),
            ],
        ),
        migrations.CreateModel(
            name='Yxjjlex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mixvrbh', models.OneToOneField(null=True, related_name='+', to='ftcfrcnas.Qrwqtj')),
            ],
        ),
        migrations.CreateModel(
            name='Zhgafcksok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mxvgvvi', models.OneToOneField(null=True, related_name='+', to='glcmkwkzv.Idmamodyjp')),
            ],
        ),
    ]
