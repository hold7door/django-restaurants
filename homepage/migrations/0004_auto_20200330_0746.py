# Generated by Django 2.2.6 on 2020-03-30 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200330_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-AggregateRating']},
        ),
    ]
