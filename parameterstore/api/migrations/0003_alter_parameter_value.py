# Generated by Django 4.1.1 on 2022-09-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_parameter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='value',
            field=models.CharField(max_length=256),
        ),
    ]
