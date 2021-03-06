# Generated by Django 4.0.1 on 2022-01-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_channels_master_channels_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='channels',
            name='channel_pic',
            field=models.FileField(default='', upload_to='channel_pic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos'),
        ),
    ]
