# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0007_yjzzdopc'),
        ('digmcd', '0017_auto_20150218_1628'),
        ('emncdxt', '0010_gnxmv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ggnqplqy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ijiinakbf', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='mioxdvg',
            name='rzvpibb',
        ),
        migrations.RemoveField(
            model_name='shgjep',
            name='lxxaql',
        ),
        migrations.AddField(
            model_name='mioxdvg',
            name='xnynvbsy',
            field=models.OneToOneField(null=True, related_name='+', to='digmcd.Xmvhvzui'),
        ),
        migrations.AddField(
            model_name='shgjep',
            name='ceinb',
            field=models.CharField(default='', max_length=203),
        ),
        migrations.AddField(
            model_name='yvgnpangr',
            name='pibin',
            field=models.OneToOneField(null=True, related_name='+', to='rwlfplwktj.Thqldbdjm'),
        ),
    ]
