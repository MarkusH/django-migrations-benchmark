# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsrp', '0001_initial'),
        ('ygnakzgjxu', '0001_initial'),
        ('bniworfy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iowgy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kffkvcz', models.CharField(default='', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Lfssmpr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udrjcs', models.OneToOneField(null=True, related_name='+', to='ygnakzgjxu.Mxlpodxpm')),
            ],
        ),
        migrations.CreateModel(
            name='Nizqeesp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eijzug', models.OneToOneField(null=True, related_name='+', to='bniworfy.Trjyk')),
            ],
        ),
        migrations.CreateModel(
            name='Oyjnlgzy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qmfhtty', models.CharField(default='', max_length=216)),
            ],
        ),
        migrations.CreateModel(
            name='Uodtjnez',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasnn', models.OneToOneField(null=True, related_name='+', to='bniworfy.Dkvkm')),
            ],
        ),
        migrations.CreateModel(
            name='Yusanbjmh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jskimt', models.ForeignKey(null=True, related_name='+', to='cmsrp.Ncysy')),
            ],
        ),
    ]
