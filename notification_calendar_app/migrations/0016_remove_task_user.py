# Generated by Django 3.1.2 on 2020-10-22 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification_calendar_app', '0015_auto_20201022_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
