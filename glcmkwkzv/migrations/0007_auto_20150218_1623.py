# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0006_delete_hbsqbahnce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lowamdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glcfis', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='iwzqe',
            name='smyorbp',
        ),
        migrations.AddField(
            model_name='iwzqe',
            name='udpsgi',
            field=models.IntegerField(default=0),
        ),
    ]
