# Generated by Django 4.1.7 on 2023-03-29 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massege',
            new_name='messege',
        ),
    ]