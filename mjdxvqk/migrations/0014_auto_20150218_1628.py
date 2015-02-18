# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avwpufexob', '0013_auto_20150218_1628'),
        ('zngxahi', '0015_auto_20150218_1628'),
        ('mjdxvqk', '0013_auto_20150218_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fvzjaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rlycrvp', models.OneToOneField(null=True, related_name='+', to='zngxahi.Qahkfonewx')),
            ],
        ),
        migrations.RemoveField(
            model_name='xglneni',
            name='ltnmc',
        ),
        migrations.AddField(
            model_name='curcmm',
            name='ekuemci',
            field=models.OneToOneField(null=True, related_name='+', to='avwpufexob.Vxucuqwa'),
        ),
        migrations.DeleteModel(
            name='Xglneni',
        ),
    ]
