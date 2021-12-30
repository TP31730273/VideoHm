from django.shortcuts import render,redirect

from .models import *

# default data dictionary
default_data ={

}
# Create your views here.
def register(request):
    return render(request,'app/register.html')

def login(request):
    return render(request,'app/login.html')

def forgot_password(request):
    return render(request,'app/forgot-password.html')

def home(request):
    profile_data(request)
    return render(request,'app/index.html')

# profile data function
def profile_data(request):
    master= Master.objects.get(mobile_no=request.session['mobile'])
    profile=Profile.objects.get(Master= master)
    print(request.session['mobile'])
    

    default_data['profile_data']=profile
# register data function

def register_data(request):
    master=Master.objects.create(
        Email=request.POST['email'],     
        mobile_no=request.POST['mobile'],     
        password=request.POST['password']

    )
    request.session['email']=request.POST['email']
    Profile.objects.create(Master=master)
    
    return redirect(register)

# login data function

def login_data(request):
    mobile=request.POST['mobile']
    password=request.POST['password']

    master=Master.objects.get(mobile_no=mobile)
    if master.password == password:
        request.session['mobile']=mobile
        print("login success",master)
        return redirect(home)
    else:
        msg="user does not exist register first"
        print(msg)
    return redirect(login)

# logout function
def signout(request):
    if 'mobile' in request.session:
        del request.session
    return redirect(login)