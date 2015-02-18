# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavygg', '0016_auto_20150218_1631'),
        ('etnevwmkj', '0013_noxqha_rwbzlshdc'),
        ('ftcfrcnas', '0020_auto_20150218_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mblprepscx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lovkg', models.ForeignKey(null=True, related_name='+', to='zavygg.Jydvnf')),
            ],
        ),
        migrations.RemoveField(
            model_name='sukkrqb',
            name='lbyzkekw',
        ),
        migrations.AddField(
            model_name='sukkrqb',
            name='slilak',
            field=models.ForeignKey(null=True, related_name='+', to='etnevwmkj.Ryfwmkefy'),
        ),
    ]
