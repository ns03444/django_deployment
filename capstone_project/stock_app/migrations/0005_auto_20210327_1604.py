# Generated by Django 3.1.7 on 2021-03-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0004_auto_20210327_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
