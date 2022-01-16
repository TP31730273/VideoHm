from django.contrib import admin

from .models import Master, Profile, Channels, Video


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


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Master',
        'channel_name',
        'subscribers',
        'following',
        'catagory',
    )
    list_filter = ('Master',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'channel_name',
        'Video_Title',
        'video',
        'thumbnail',
        'About',
        'Language',
        'cast',
        'category',
    )
    list_filter = ('channel_name',)