# Generated by Django 3.0.2 on 2020-03-01 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200227_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pubg_info',
            name='user',
        ),
    ]