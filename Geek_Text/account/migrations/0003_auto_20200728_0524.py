# Generated by Django 3.0.8 on 2020-07-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200728_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_ccv',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='card_name',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=models.CharField(max_length=26),
        ),
    ]