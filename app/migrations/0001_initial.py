# Generated by Django 4.0.1 on 2022-01-14 20:43

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=18, unique=True)),
                ('Email', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=18)),
            ],
            options={
                'db_table': 'master',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_Title', models.CharField(default='', max_length=100, null=True)),
                ('video', models.FileField(default='settings.MEDIA_ROOT/logos/download.jpg', storage=django.core.files.storage.FileSystemStorage(location='D:\\D\\youtube\\media'), upload_to='video')),
                ('About', models.TextField(default='', max_length=350, null=True)),
                ('Language', models.CharField(default='', max_length=350, null=True)),
                ('cast', models.CharField(default='', max_length=350, null=True)),
                ('category', models.CharField(default='', max_length=150, null=True)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.master')),
            ],
            options={
                'db_table': 'Video',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(default='', max_length=30, null=True)),
                ('Mobile', models.CharField(default='', max_length=30, null=True)),
                ('Country', models.CharField(default='', max_length=10, null=True)),
                ('City', models.CharField(default='', max_length=25, null=True)),
                ('Address', models.TextField(default='', max_length=150, null=True)),
                ('Zip', models.TextField(default='', max_length=150, null=True)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.master')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
