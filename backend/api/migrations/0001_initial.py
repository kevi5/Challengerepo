# Generated by Django 4.1.5 on 2024-02-22 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('copies', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Circulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returnevent', models.BooleanField(default=False)),
                ('book_id', models.IntegerField()),
                ('member_id', models.IntegerField()),
                ('date', models.DateField(default=datetime.time(5, 24, 46, 910485))),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=100)),
            ],
        ),
    ]
