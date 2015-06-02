# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realityquest', '0002_auto_20150513_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('mission_briefing', models.CharField(default=b'', max_length=128)),
                ('start_quote', models.CharField(default=b'', max_length=128)),
                ('end_quote', models.CharField(default=b'', max_length=128)),
                ('end_with', models.ForeignKey(related_name=b'end_with', to='realityquest.NPC')),
                ('start_with', models.ForeignKey(related_name=b'start_with', to='realityquest.NPC')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='quote',
            name='text',
            field=models.CharField(default=b"What's up?", max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quote',
            name='npc',
            field=models.ForeignKey(to='realityquest.NPC'),
        ),
    ]
