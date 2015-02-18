# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joavhqi', '0012_auto_20150218_1626'),
        ('epbbfwihj', '0014_auto_20150218_1627'),
        ('zngxahi', '0013_auto_20150218_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kdfltvrrbx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixyrsm', models.CharField(default='', max_length=36)),
            ],
        ),
        migrations.AddField(
            model_name='eauslyif',
            name='uosdpbua',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hiqedajgiu',
            name='pvjgvt',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='qmhypaufcg',
            name='jydjg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vnoruiao',
            name='filiupvrkr',
            field=models.ForeignKey(null=True, related_name='+', to='epbbfwihj.Uzdthbetj'),
        ),
        migrations.AddField(
            model_name='xrrtgf',
            name='prtbwzl',
            field=models.OneToOneField(null=True, related_name='+', to='joavhqi.Oyjnlgzy'),
        ),
    ]
