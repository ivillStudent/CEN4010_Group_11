  
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_details', '0005_auto_20180331_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='portrait',
            field=models.ImageField(null=True, upload_to='author_portraits/', verbose_name='Portrait of Author'),
        ),
    ]