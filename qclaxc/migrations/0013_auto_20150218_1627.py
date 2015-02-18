# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ysgxuyu', '0009_remove_bmovnbnmed_cmnup'),
        ('qclaxc', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pjboumq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lkywyq', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Ladoumxyr',
        ),
        migrations.RemoveField(
            model_name='yswziiulyl',
            name='vliqzzx',
        ),
        migrations.AddField(
            model_name='ggafntnbq',
            name='ergswy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='yiifw',
            name='ufrqn',
            field=models.OneToOneField(null=True, related_name='+', to='ysgxuyu.Njigbqwuqa'),
        ),
    ]
