# Generated by Django 3.1 on 2021-02-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=64, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'DataList',
            },
        ),
        migrations.CreateModel(
            name='DataStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_name', models.CharField(max_length=20)),
                ('stream_para', models.IntegerField(default=0, null=True)),
                ('limit', models.FloatField(blank=True, default=0, null=True)),
                ('qos', models.IntegerField(default=0, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('unit_symbol', models.CharField(blank=True, max_length=10, null=True)),
                ('data', models.ManyToManyField(blank=True, null=True, to='website.Data')),
            ],
            options={
                'db_table': 'StreamList',
            },
        ),
    ]
