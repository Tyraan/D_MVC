# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='descripton',
            new_name='description',
        ),
    ]
