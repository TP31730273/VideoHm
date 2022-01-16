from django.urls import path
from videohm.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('',login ,name="login"),
    path('register/',register ,name="register"),
    path('forgot_pass/',forgot_password ,name="forgot_pass"),
    path('home/',home ,name="home"),
# functional urls
    path('register_data/',register_data ,name="register_data"),
    path('login_data/',login_data ,name="login_data"),
    path('signout/',signout ,name="signout"),
    path('profile_setting/',profile_setting ,name="profile_setting"),
    path('My_account/',My_account ,name="My_account"),
    path('Upload/',Upload ,name="Upload"),
    path('settings/',setting ,name="settings"),
    # path('v_page/',v_page ,name="v_page"),

    
    path('video_page/<int:vid>/',video_page ,name="video_page"),
    # actual upload page
    path('upload_page/',upload_page ,name="upload_page"),
    # upload process url
    path('upload_process/',upload_process ,name="upload_process"),
   
   

]


