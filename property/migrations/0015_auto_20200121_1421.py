# Generated by Django 2.2.3 on 2020-01-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20200117_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_pure',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
