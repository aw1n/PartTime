# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0001_initial'),
        ('offers', '0003_auto_20140930_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='company',
            name='company_user',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='user_timezone',
            field=models.CharField(default=b'Europe/London', max_length=50),
            preserve_default=True,
        ),
    ]
