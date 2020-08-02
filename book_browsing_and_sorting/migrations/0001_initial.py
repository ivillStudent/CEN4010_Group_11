# Generated by Django 3.0.8 on 2020-08-02 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookdetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='browsingGenre', to='bookdetails.BookInfo')),
            ],
        ),
    ]