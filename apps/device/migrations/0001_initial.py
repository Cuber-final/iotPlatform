# Generated by Django 3.1 on 2021-02-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('device_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('tag', models.CharField(blank=True, max_length=32, null=True)),
                ('device_key', models.CharField(blank=True, max_length=32, null=True)),
                ('device_name', models.CharField(blank=True, max_length=32, null=True)),
                ('dev_status', models.BooleanField(default=0)),
                ('creative_date', models.DateTimeField(auto_now_add=True)),
                ('protocol', models.CharField(default='mqtt', max_length=10, null=True)),
                ('dev_stream', models.ManyToManyField(blank=True, null=True, to='website.DataStream')),
            ],
            options={
                'db_table': 'deviceInfo',
            },
        ),
    ]
