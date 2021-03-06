# Generated by Django 2.0.6 on 2018-06-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180621_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('app_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('app_key', models.CharField(max_length=100)),
                ('session_key', models.CharField(max_length=100)),
                ('app_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('sport_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sport_name', models.CharField(max_length=10, primary_key=True)),
                ('market_count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
