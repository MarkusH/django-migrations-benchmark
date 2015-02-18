# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rwlfplwktj', '0007_yjzzdopc'),
        ('glcmkwkzv', '0013_delete_unnork'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bckfaijv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xqseghhj', models.ForeignKey(null=True, related_name='+', to='rwlfplwktj.Yjzzdopc')),
            ],
        ),
        migrations.RemoveField(
            model_name='vkgguay',
            name='lnfahjzeib',
        ),
        migrations.DeleteModel(
            name='Vkgguay',
        ),
    ]
