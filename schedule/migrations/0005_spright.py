# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_text_fields_not_null'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
