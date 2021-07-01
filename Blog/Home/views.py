from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Feedback
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeedbackSerializer,PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
@api_view(['GET'])
def Index(request):
    post=Post.objects.all()
    serializer=PostSerializer(post,many=True)  
    context={ 
        'posts':serializer.data
    }
    return render(request,'index.html',context)
    
def About(request):
    return render(request,'about.html') 

  
def Contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']
        message=request.POST['message']
        singleRow=Feedback(name=name,phone=phone,message=message,email=email)
        singleRow.save()
        messages.success(request, 'Your Message has been sent to the admin')
    else:
        return render(request,"contact.html")
    return render(request,'contact.html')
@api_view(['GET'])
def SinglePost(request,idOfPost):
    post=Post.objects.filter(id=idOfPost)
    serializer= PostSerializer(post,many=True)
    
    context={
        'singlePost':serializer.data[0],
    }
    return render(request,'post.html',context)
def Login(request):
    return render(request,'login.html')
def home(request):
    post=Post.objects.all()
    serializer=PostSerializer(post,many=True)  
    context={ 
        'posts':serializer.data
    }
    return render(request,'index.html',context)