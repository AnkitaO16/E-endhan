# Generated by Django 3.2.4 on 2022-04-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20220422_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='email',
            field=models.EmailField(max_length=300),
        ),
        migrations.AlterField(
            model_name='destination',
            name='fuel',
            field=models.CharField(max_length=300),
        ),
    ]
