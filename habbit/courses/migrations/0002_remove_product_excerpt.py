# Generated by Django 3.2.4 on 2021-06-17 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='excerpt',
        ),
    ]
