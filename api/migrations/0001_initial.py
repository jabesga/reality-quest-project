# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('portrait_style', models.IntegerField(default=0, max_length=128)),
                ('lat', models.FloatField(default=0, max_length=128)),
                ('lng', models.FloatField(default=0, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('npc', models.ForeignKey(to='realityquest.NPC')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
