# Generated by Django 4.0.1 on 2022-01-17 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_channels_channel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='channel_name',
            new_name='channel',
        ),
    ]