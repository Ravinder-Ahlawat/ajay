# Generated by Django 2.2.2 on 2020-03-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0006_auto_20200303_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='order_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]