# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0008_auto_20150218_1630'),
        ('joavhqi', '0013_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sabdmpl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leietkf', models.OneToOneField(null=True, related_name='+', to='zsskgviadw.Ltlsozji')),
            ],
        ),
    ]
