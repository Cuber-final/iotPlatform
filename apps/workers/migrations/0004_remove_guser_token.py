# Generated by Django 3.1 on 2021-02-07 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_guser_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guser',
            name='token',
        ),
    ]