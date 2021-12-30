from django.urls import path
from .views import *

urlpatterns = [
    path('',login ,name="login"),
    path('register/',register ,name="register"),
    path('forgot_pass/',forgot_password ,name="forgot_pass"),
    path('home/',home ,name="home"),
# functional urls
    path('register_data/',register_data ,name="register_data"),
    path('login_data/',login_data ,name="login_data"),
    path('signout/',signout ,name="signout"),

]

