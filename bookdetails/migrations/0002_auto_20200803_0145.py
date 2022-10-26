# Generated by Django 3.0.8 on 2020-08-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookdetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bookName',
            field=models.CharField(default='name', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='copiesSold',
            field=models.CharField(default=0, max_length=100000000),
        ),
    ]