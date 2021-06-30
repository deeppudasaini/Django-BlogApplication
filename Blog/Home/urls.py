from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
path('',views.Index,name="Home Page"),
path('home',views.home,name="Home"),
path('login',views.Login,name="Login"),
path('contact',views.Contact,name="Contact"),
path('about',views.About,name="About"),
path('post/<int:idOfPost>/',views.SinglePost,name="Post"),
]
