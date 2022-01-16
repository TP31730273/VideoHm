# Generated by Django 4.0.1 on 2022-01-16 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_channels_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='channels',
        ),
        migrations.AddField(
            model_name='video',
            name='channel_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.channels'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='channels',
            name='following',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='channels',
            name='subscribers',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
