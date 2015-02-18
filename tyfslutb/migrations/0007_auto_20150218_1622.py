# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0007_delete_aivqb'),
        ('tyfslutb', '0006_ynbpgqn_pgbxqxfrn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vzqlh',
            name='rdeaj',
        ),
        migrations.RemoveField(
            model_name='ynbpgqn',
            name='pgbxqxfrn',
        ),
        migrations.AddField(
            model_name='ynbpgqn',
            name='rtmpcyteit',
            field=models.ForeignKey(null=True, related_name='+', to='kakry.Aefqhqkmm'),
        ),
        migrations.DeleteModel(
            name='Vzqlh',
        ),
    ]
