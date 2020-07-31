# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_details', '0002_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='book_covers/', verbose_name='Front cover of book'),
        ),
    ]