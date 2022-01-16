from django.contrib import admin

from .models import Master, Profile, Video


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile_no', 'Email', 'password')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Master',
        'FullName',
        'Mobile',
        'Country',
        'City',
        'Address',
        'Zip',
    )
    list_filter = ('Master',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Master',
        'Video_Title',
        'video',
        'About',
        'Language',
        'cast',
        'category',
    )
    list_filter = ('Master',)