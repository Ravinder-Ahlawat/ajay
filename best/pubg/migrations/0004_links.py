# Generated by Django 3.0.2 on 2020-03-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubg', '0003_join'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
    ]