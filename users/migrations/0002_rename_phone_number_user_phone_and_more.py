# Generated by Django 4.2.4 on 2023-09-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_roles',
            new_name='roles',
        ),
    ]
