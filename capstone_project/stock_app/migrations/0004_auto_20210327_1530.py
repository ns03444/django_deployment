# Generated by Django 3.1.7 on 2021-03-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0003_auto_20210327_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(max_length=10),
        ),
    ]
