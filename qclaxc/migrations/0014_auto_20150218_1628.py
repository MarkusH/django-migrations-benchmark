# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0010_auto_20150218_1628'),
        ('qclaxc', '0013_auto_20150218_1627'),
    ]

    run_before = [
        ('ysgxuyu', '0012_delete_bmovnbnmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ilngaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rhjodfszjd', models.ForeignKey(null=True, related_name='+', to='ysgxuyu.Bmovnbnmed')),
            ],
        ),
        migrations.RemoveField(
            model_name='ggafntnbq',
            name='ergswy',
        ),
        migrations.RemoveField(
            model_name='ooecads',
            name='nflopwecc',
        ),
    ]
