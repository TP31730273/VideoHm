from doctest import master
import profile
import re
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *

# default data dictionary
default_data = {

}
# Create your views here.


def register(request):
    return render(request, 'app/register.html')
# normal upload page


def Upload(request):
    return render(request, 'app/upload.html')

# all channels showing


def channels(request):
    profile_data(request)
    return render(request, 'app/channels.html', default_data)

# my channel page


def My_channel(request):
    profile_data(request)

    return render(request, 'app/personal-channel.html', default_data)

# clicked channel


def single_channel(request, cid):
    profile_data(request)
    selected_channel = Channels.objects.get(id=cid)
    selected_channel_videos = Video.objects.filter(channel=selected_channel)
    default_data['selected_channel'] = selected_channel
    default_data['selected_channel_videos'] = selected_channel_videos
    return render(request, 'app/single-channel.html', default_data)


def create_channel_page(request):
    return render(request, 'app/create_channel.html')
# actual upload page of process


def upload_page(request):
    profile_data(request)

    return render(request, 'app/upload-video.html', default_data)


def video_page(request, vid):
    profile_data(request)
    selected_vid = Video.objects.get(id=vid)
    print("selected_vid.video", selected_vid.video)
    default_data['selected_video'] = selected_vid

    return render(request, 'app/video-page.html', default_data)

# def v_page(request):
#     profile_data(request)

#     return render(request,'app/video-page.html',default_data)


def setting(request):
    profile_data(request)
    return render(request, 'app/settings.html', default_data)


def login(request):
    if 'mobile' in request.session:
        return redirect(home)
    default_data['current_page'] = 'login'
    return render(request, 'app/login.html', default_data)


def forgot_password(request):
    return render(request, 'app/forgot-password.html')


def My_account(request):
    profile_data(request)
    return render(request, 'app/account.html', default_data)


def home(request):
    profile_data(request)
    return render(request, 'app/index.html', default_data)


# profile data function
def profile_data(request):
    master = Master.objects.get(mobile_no=request.session['mobile'])
    profile = Profile.objects.get(Master=master)
    print(request.session['mobile'])
    # upload_process(request)

    all_videos(request)
    show_all_channels(request)
    try:
        current_channel_data(request)
        show__my_videos(request)
        print("channel present")
    except:
        print("channel not present")
    default_data['profile_data'] = profile
    

# register data function


def register_data(request):
    master = Master.objects.create(
        Email=request.POST['email'],
        mobile_no=request.POST['mobile'],
        password=request.POST['password']

    )
    Profile.objects.create(Master=master)

    return redirect(register)


# logged_in person's channel data
def current_channel_data(request):
    chan = Channels.objects.get(Profile=(
        Profile.objects.get(
            Master=(
                Master.objects.get(mobile_no=request.session['mobile'])
            )
        )
    ))
    default_data['current_channel'] = chan

# create channel data


def Create_channel(request):
    cl_pic=request.FILES['C_pic']
    chan = Channels.objects.create(
        Profile=(
            Profile.objects.get(Master=(
                Master.objects.get(mobile_no=request.session['mobile'])
            ))),
        channel_name=request.POST['cname'],
        catagory=request.POST['category'],
        Channel_pic=cl_pic)
    chan.save()
    request.session['Mychannel'] = chan.channel_name
    return redirect(home)


# login data function

def login_data(request):
    mobile = request.POST['mobile']
    master = Master.objects.get(mobile_no=mobile)
    prof = Profile.objects.get(Master=master)

    try:

        try:

            print("mast:", master)
            chn = Channels.objects.get(Profile=prof)
            print("you have channel go on :", request.session['Mychannel'])
        except:
            print("you don't have channel")

        if master.password == request.POST['password']:
            request.session['mobile'] = mobile

            print("login success", master)
            return redirect(home)
        else:
            msg = "user does not exist register first"
            print(msg)
    except:
        print(f"user does not exist please register it.")
    return redirect(login)

# profile settings


def profile_setting(request):
    master = Master.objects.get(mobile_no=request.session['mobile'])
    profile = Profile.objects.get(Master=master)
    profile.FullName = request.POST['fname']
    profile.Country = request.POST['country']
    profile.City = request.POST['city']
    profile.Address = request.POST['address']
    profile.Zip = request.POST['zip']
    profile.Mobile = request.session['mobile']
    profile.save()
    profile_data(request)

    return redirect(setting)

# logout function


def signout(request):
    if 'mobile' in request.session:
        print(request.session)
        del request.session['mobile']
    # if 'Mychannel' in request.session:
    #     del request.session['Mychannel']
    print('logout')
    return redirect(login)

# upload video


def upload_process(request):
    chan = Channels.objects.get(Profile=(
        Profile.objects.get(Master=(
            Master.objects.get(mobile_no=request.session['mobile'])
        ))
    ))
    vidoo = request.FILES['video']
    thumb = request.FILES['thumbnail']
    print(vidoo)
    vid = Video.objects.create(channel=chan, Video_Title=request.POST['vtitle'], video=vidoo, thumbnail=thumb, About=request.POST[
                               'about'], cast=request.POST['cast'], category=request.POST['category'], Language=request.POST['language'])
    vid.save()

    # video.Language=request.POST['language']
    # video.Language=request.POST['language']
    # video.
    return redirect(My_channel)

# video showing page


def show__my_videos(request):
    video = Video.objects.filter(
        channel=(Channels.objects.get(
            Profile=(
                Profile.objects.get(
                    Master=(
                        Master.objects.get(mobile_no=request.session['mobile'])))))))
    default_data['myvideo'] = video
    print("my videos: ", video)


def all_videos(request):
    allvideos = Video.objects.all()
    default_data['all_videos'] = allvideos
    # print(allvideos)


def show_all_channels(request):
    chn = Channels.objects.all()
    default_data['all_channels'] = chn


def subscribers(request):
    s = Subscriptions.objects.all()
    l1 = []
    channel = []
    for i in s:
        l1.append([i.Master.mobile_no, i.subscribed_channel.channel_name])
        channel.append(i.subscribed_channel.channel_name)
    print(l1)
    channel = list(set(channel))
    print(channel)
    sub_dict = {}
    for i in channel:
        sum = 0
        for j in l1:
            if i in j:
                sum = sum+1
        sub_dict[i] = sum
    print(sub_dict)
    chn = Channels.objects.all()
    for i in chn:
        for j in sub_dict:
            if i.channel_name == j:
                chu = Channels.objects.get(channel_name=j)
                chu.subscribers = sub_dict[j]
                chu.save()
