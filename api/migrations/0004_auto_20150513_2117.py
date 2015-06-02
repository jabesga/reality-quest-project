# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realityquest', '0003_auto_20150513_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='text',
            new_name='quora',
        ),
    ]
