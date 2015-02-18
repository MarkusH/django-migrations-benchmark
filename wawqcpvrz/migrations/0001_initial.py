# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsrp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ndmxpw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narpapscx', models.ForeignKey(null=True, related_name='+', to='cmsrp.Ncysy')),
            ],
        ),
        migrations.CreateModel(
            name='Nrmckl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yrmez', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Scfuekgkl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wglslgn', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Schqt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mwqwibfn', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tyhxj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afzkaucmga', models.CharField(default='', max_length=73)),
            ],
        ),
        migrations.CreateModel(
            name='Vrvslusmy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qbmyulpzc', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Xivomw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdxup', models.CharField(default='', max_length=202)),
            ],
        ),
        migrations.CreateModel(
            name='Ydfkef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdhaftsm', models.CharField(default='', max_length=48)),
            ],
        ),
    ]
