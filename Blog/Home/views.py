from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Feedback
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeedbackSerializer,PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
def register(request):
    if request.method=='POST':
        CLIENT_SECRET_FILE = 'credentials.json'
        API_NAME = 'gmail'
        API_VERSION = 'v1'
        SCOPES = ['https://mail.google.com/']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        emailMsg = 'Hello '+request.POST['full']+',\n\nWe have provided you with your username and password to access the Daily Post.\n\n'+'Username:'+ '\n\nPassword:'+'\n\nYour Email will be soon validiated and given access. \n\nPlease until another mail pops up.\n\n\n Thank you!'
        mimeMessage = MIMEMultipart() 
        mimeMessage['to'] = request.POST['reg-email']
        mimeMessage['subject'] = 'Username and Password from Daily Post'
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    else:
         return redirect('login')        
    return render(request,'login.html')
        