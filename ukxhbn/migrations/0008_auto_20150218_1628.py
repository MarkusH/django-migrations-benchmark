# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyfslutb', '0017_remove_ihswfvupi_ywstkx'),
        ('zhavbmq', '0016_mkihzu'),
        ('ukxhbn', '0007_auto_20150218_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aciaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xjwwdbi', models.OneToOneField(null=True, related_name='+', to='tyfslutb.Ynbpgqn')),
            ],
        ),
        migrations.RemoveField(
            model_name='qujmudiaaa',
            name='gjisrcwtgs',
        ),
        migrations.AddField(
            model_name='qujmudiaaa',
            name='golxts',
            field=models.CharField(default='', max_length=229),
        ),
        migrations.AddField(
            model_name='xqerjvxatp',
            name='kjyjccxd',
            field=models.ForeignKey(null=True, related_name='+', to='zhavbmq.Ulvookvun'),
        ),
    ]
