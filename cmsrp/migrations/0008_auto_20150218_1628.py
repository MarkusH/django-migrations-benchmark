# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnxyvqx', '0011_ecatm'),
        ('cmsrp', '0007_auto_20150218_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vlmfay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fejusiz', models.OneToOneField(null=True, related_name='+', to='pnxyvqx.Nenfvguk')),
            ],
        ),
        migrations.DeleteModel(
            name='Dtpkzlh',
        ),
    ]
