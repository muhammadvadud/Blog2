# Generated by Django 4.1.7 on 2023-03-31 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0012_rename_massege_contact_messege'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messege',
            new_name='message',
        ),
    ]
