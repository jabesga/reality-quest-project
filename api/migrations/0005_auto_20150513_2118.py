# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realityquest', '0004_auto_20150513_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quora',
            new_name='quote',
        ),
    ]
