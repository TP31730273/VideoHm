# Generated by Django 4.0.1 on 2022-01-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_channels_channel_pic_alter_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channels',
            name='channel_pic',
        ),
        migrations.AddField(
            model_name='channels',
            name='Channel_pic',
            field=models.FileField(default='', upload_to='channel_pic'),
            preserve_default=False,
        ),
    ]
