# Generated by Django 4.0.1 on 2022-01-19 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_channels_channel_pic_channels_channel_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptions',
            name='Master',
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='comments_and_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.video')),
            ],
            options={
                'db_table': 'Comments_and_likes',
            },
        ),
    ]
