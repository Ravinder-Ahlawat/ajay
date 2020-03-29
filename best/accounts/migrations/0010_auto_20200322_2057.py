# Generated by Django 2.2.2 on 2020-03-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_userdetails_pubg_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('pubg_id', models.CharField(blank=True, max_length=11)),
                ('pubg_name', models.CharField(blank=True, max_length=20)),
                ('user', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
        migrations.DeleteModel(
            name='wirthdraw',
        ),
    ]
