# Generated by Django 3.1.6 on 2021-06-05 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='useremail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='message',
            new_name='feedback',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='usernum',
            new_name='number',
        ),
    ]
