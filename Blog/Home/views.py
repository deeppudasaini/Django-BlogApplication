from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Feedback,Staff
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeedbackSerializer,PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .Google import Create_Service
import base64,os
import random
from twilio.rest import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime,random,string
# Create your views here.
@api_view(['GET'])
def Index(request):
    return redirect('/home')
    
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
def LoginCheck(request):
    if request.method=='POST':

        u=request.POST['user']
        p=request.POST['pass']
        user = authenticate(username=u, password=p)
        
        if user is not None:
            #OTP sample
            # account_sid = 'ACc20b0e9e17dddde87c26c777c27071b6'
            # auth_token = 'f8f146d82b7eea13f7577c1111da11e6'
            # client = Client(account_sid, auth_token)
            # otpp='12345';
            # message = client.messages \
            #     .create(
            #         messaging_service_sid='MG9752274e9e519418a7406176694466fa',
            #         body='Please Verify by entering below OTP\n'+otpp,
            #         to='+9779863336834'#Sample Number
            #     )
            # print(message.sid)
            otpp=random(6);
            CLIENT_SECRET_FILE = 'credentials.json'
            API_NAME = 'gmail'
            API_VERSION = 'v1'
            SCOPES = ['https://mail.google.com/']
            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
            emailMsg = 'Hello '+u+' \n Your OTP is ' + otpp
            mimeMessage = MIMEMultipart() 
            mimeMessage['to'] = User.objects.filter(username=u)
            mimeMessage['subject'] = 'OTP Verification'
            mimeMessage.attach(MIMEText(emailMsg, 'plain'))
            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            messages.success(request, 'Please check your email for your OTP')
            if request.method=='post':
                if request.POST['otp']==otpp:
                    login(request,user)                
                    return redirect("/home")
                else:
                    return render(request,'login.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
@api_view(['GET'])
def home(request):
    post=Post.objects.all()
    serializer=PostSerializer(post,many=True)  
    context={ 
        'posts':serializer.data
    }
    return render(request,'index.html',context)
    
def About(request):
    return render(request,'about.html') 
def register(request):
    if request.method=='POST':
        # if Staff.objects.filter(email=request.POST['reg-email']).exists():
        #     messages.danger(request, 'Email has been already registered')
        # else: 
            name=request.POST['full']
            email=request.POST['reg-email']
            
            x = datetime.datetime.now()
            username='dailypost'+str(x.year)+str(len(Staff.objects.all())+1)
            password=str(random.sample((string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation),12));
            singleRow=Staff(name=name,email=email,username=username,password=password)
            singleRow.save()
            staffuser=User.objects.create_user(username=username,email=email,password=password)
            
            staffuser.save()
            staffuser.user_permission.set([])
            CLIENT_SECRET_FILE = 'credentials.json'
            API_NAME = 'gmail'
            API_VERSION = 'v1'
            SCOPES = ['https://mail.google.com/']
            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
            emailMsg = 'Hello '+name+',\n\nWe have provided you with your username and password to access the Daily Post.\n\n'+'Username: '+username+ '\n\nPassword: '+password+'\n\nYour Email will be soon validiated and given access. \n\nPlease until another mail pops up.\n\n\n Thank you!'
            mimeMessage = MIMEMultipart() 
            mimeMessage['to'] = request.POST['reg-email']
            mimeMessage['subject'] = 'Username and Password from Daily Post'
            mimeMessage.attach(MIMEText(emailMsg, 'plain'))
            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            messages.success(request, 'Please check your email for your email and password')
    else:
         return render(request,'login.h tml')        
    return render(request,'login.html')
def exit(request):
    logout(request)
    return redirect('/login')
