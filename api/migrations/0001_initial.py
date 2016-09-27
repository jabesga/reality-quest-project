# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('mission_briefing', models.CharField(default='', max_length=128)),
                ('start_quote', models.CharField(default='', max_length=128)),
                ('end_quote', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('portrait_style', models.IntegerField(default=0)),
                ('lat', models.FloatField(default=0, max_length=128)),
                ('lng', models.FloatField(default=0, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(default="What's up?", max_length=128)),
                ('npc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NPC')),
            ],
        ),
        migrations.AddField(
            model_name='mission',
            name='end_with',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_with', to='api.NPC'),
        ),
        migrations.AddField(
            model_name='mission',
            name='start_with',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_with', to='api.NPC'),
        ),
    ]
