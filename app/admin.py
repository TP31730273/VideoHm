from django.contrib import admin

from .models import Master, Profile, Channels, Video, Subscriptions, comments_and_likes


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
        'Profile',
        'channel_name',
        'subscribers',
        'following',
        'catagory',
        'Channel_pic',
    )
    list_filter = ('Profile',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'channel',
        'Video_Title',
        'video',
        'thumbnail',
        'About',
        'Language',
        'cast',
        'category',
    )
    list_filter = ('channel',)


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'subscribed_channel')
    list_filter = ('profile', 'subscribed_channel')


@admin.register(comments_and_likes)
class comments_and_likesAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile','channel', 'video',  'comments')
    list_filter = ('profile', 'video', 'channel')