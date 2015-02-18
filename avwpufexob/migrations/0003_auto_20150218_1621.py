# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avwpufexob', '0002_yejdqycpmg_gppos'),
        ('zsskgviadw', '0001_initial'),
        ('wawqcpvrz', '0001_initial'),
        ('zxxavsovs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubpmj',
            name='ktwasnimoe',
            field=models.OneToOneField(null=True, related_name='+', to='zsskgviadw.Hcetattb'),
        ),
        migrations.AddField(
            model_name='nhpkrhkql',
            name='gphdl',
            field=models.ForeignKey(null=True, related_name='+', to='wawqcpvrz.Tyhxj'),
        ),
        migrations.AddField(
            model_name='fvlkcjd',
            name='onlvfzdsk',
            field=models.ForeignKey(null=True, related_name='+', to='zxxavsovs.Kiikphbz'),
        ),
    ]
