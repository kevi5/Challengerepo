# Generated by Django 4.1.5 on 2024-02-22 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_circulation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circulation',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
