# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_auto_20140930_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_description',
            field=models.TextField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_mail',
            field=models.EmailField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_web',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
