# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0006_delete_xcasayyn'),
        ('rwlfplwktj', '0006_auto_20150218_1624'),
        ('wyxbcga', '0008_auto_20150218_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oblwdacdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snjlwam', models.OneToOneField(null=True, related_name='+', to='wulegwfs.Yxsnty')),
            ],
        ),
        migrations.DeleteModel(
            name='Qimzrcecmn',
        ),
        migrations.RemoveField(
            model_name='eezxvbbvmn',
            name='cjiikmfzn',
        ),
        migrations.RemoveField(
            model_name='jkjvvohe',
            name='nezwu',
        ),
        migrations.AddField(
            model_name='eezxvbbvmn',
            name='pvzewhwow',
            field=models.ForeignKey(null=True, related_name='+', to='wyxbcga.Kpjlirt'),
        ),
        migrations.AddField(
            model_name='gmclwtufhi',
            name='jdwqs',
            field=models.ForeignKey(null=True, related_name='+', to='rwlfplwktj.Thqldbdjm'),
        ),
    ]
