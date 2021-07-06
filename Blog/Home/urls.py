from django.contrib import admin
from django.urls import path,include
from . import views
from .api import RegisterApi
urlpatterns = [
path('',views.Index,name="Home Page"),
path('home',views.home,name="Home"),
path('login',views.Login,name="Login"),
path('contact',views.Contact,name="Contact"),
path('about',views.About,name="About"),
path('LoginCheck',views.LoginCheck,name="Check"),
path('post/<int:idOfPost>/',views.SinglePost,name="Post"),
path('register',views.register,name="Register"),
path('exit',views.exit,name="logout"),
path('api/reg',RegisterApi.as_view())
]
