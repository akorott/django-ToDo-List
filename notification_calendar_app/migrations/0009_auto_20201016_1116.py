# Generated by Django 3.1.2 on 2020-10-16 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification_calendar_app', '0008_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='App_User',
        ),
    ]
