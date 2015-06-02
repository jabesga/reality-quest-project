# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realityquest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='npc',
            field=models.OneToOneField(to='realityquest.NPC'),
        ),
    ]
