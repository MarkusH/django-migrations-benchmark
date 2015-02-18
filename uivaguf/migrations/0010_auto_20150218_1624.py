# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsrp', '0004_remove_ncysy_lkvgwwfoan'),
        ('uivaguf', '0009_auto_20150218_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blekqwd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jvdlv', models.OneToOneField(null=True, related_name='+', to='cmsrp.Ncysy')),
            ],
        ),
        migrations.RemoveField(
            model_name='opwgwxncp',
            name='kxmfnvxfoi',
        ),
        migrations.AddField(
            model_name='onmti',
            name='wuhvaikk',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Opwgwxncp',
        ),
    ]
