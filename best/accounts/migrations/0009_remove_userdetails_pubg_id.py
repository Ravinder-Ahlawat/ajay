# Generated by Django 2.2.2 on 2020-03-20 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200311_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='pubg_id',
        ),
    ]
