# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procat', '0002_auto_20150121_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to='cat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to='products'),
            preserve_default=True,
        ),
    ]
