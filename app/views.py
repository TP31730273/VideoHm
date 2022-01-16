import re
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import *

# default data dictionary
default_data ={

}
# Create your views here.
def register(request):
    return render(request,'app/register.html')
# normal upload page
def Upload(request):
    return render(request,'app/upload.html')
# actual upload page of process
def upload_page(request):
    profile_data(request)
    
    
    return render(request,'app/upload-video.html',default_data)
    
def video_page(request,vid):
    profile_data(request)
    selected_vid=Video.objects.get(id=vid)
    print("selected_vid.video",selected_vid.video)
    default_data['selected_video']=selected_vid
    
    return render(request,'app/video-page.html',default_data)

# def v_page(request):
#     profile_data(request)

#     return render(request,'app/video-page.html',default_data)

def setting(request):
    profile_data(request)
    return render(request,'app/settings.html',default_data)

def login(request):
    if 'mobile' in request.session:
        return redirect(home)
    default_data['current_page'] = 'login'
    return render(request,'app/login.html',default_data)

def forgot_password(request):
    return render(request,'app/forgot-password.html')

def My_account(request):
    profile_data(request)
    return render(request,'app/account.html',default_data)

def home(request):
    profile_data(request)
    return render(request,'app/index.html',default_data)


# profile data function
def profile_data(request):
    master= Master.objects.get(mobile_no=request.session['mobile'])
    profile=Profile.objects.get(Master= master)
    videoss=Video.objects.all()
    print(request.session['mobile'])
    # upload_process(request)
    show_videos(request)
    all_videos(request)
    default_data['profile_data']=profile
    default_data['videos']=videoss

# register data function

def register_data(request):
    master=Master.objects.create(
        Email=request.POST['email'],     
        mobile_no=request.POST['mobile'],     
        password=request.POST['password']

    )
   
    Profile.objects.create(Master=master)
    
    return redirect(register)

# login data function

def login_data(request):
    mobile=request.POST['mobile']
    password=request.POST['password']

    try:
        master=Master.objects.get(mobile_no=mobile)
        
        if master.password == request.POST['password']:
            request.session['mobile']=mobile
            print("login success",master)
            return redirect(home)
        else:
            msg="user does not exist register first"
            print(msg)
    except:
         print(f"user does not exist please register it.")
    return redirect(login)

# profile settings
def profile_setting(request):
    master=Master.objects.get(mobile_no=request.session['mobile'])
    profile=Profile.objects.get(Master=master)
    profile.FullName=request.POST['fname']
    profile.Country=request.POST['country']
    profile.City=request.POST['city']
    profile.Address=request.POST['address']
    profile.Zip=request.POST['zip']
    profile.Mobile=request.session['mobile']
    profile.save()
    profile_data(request)

    return redirect(setting)
    
# logout function
def signout(request):
    if 'mobile' in request.session:
        print(request.session)
        del request.session['mobile']
        print('logout')
    return redirect(login)

# upload video

def upload_process(request):
    master=Master.objects.get(mobile_no=request.session['mobile'])
    vidoo=request.FILES['video']
    thumb=request.FILES['thumbnail']
    print(vidoo)
    vid=Video.objects.create(Master=master,Video_Title=request.POST['vtitle'],video=vidoo,thumbnail=thumb,About=request.POST['about'],cast=request.POST['cast'],category=request.POST['category'],Language=request.POST['language'])
    vid.save()
    # video.Language=request.POST['language']
    # video.Language=request.POST['language']
    # video.
   
    


    return redirect(upload_page)

# video showing page
    
def show_videos(request):
    master=Master.objects.get(mobile_no=request.session['mobile'])
    video=Video.objects.filter(Master=master)
    default_data['video']=video
      
def all_videos(request):
    allvideos=Video.objects.all()
    default_data['all_videos']=allvideos
    # print(allvideos)