from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Feedback
from django.contrib import messages
# Create your views here.
def Index(request):
    context={ 
        'posts':Post.objects.all()
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
def SinglePost(request,idOfPost):
    post=Post.objects.filter(id=idOfPost)
    
    context={
        'singlePost':post[0],
        
    }
    return render(request,'post.html',context)
def Login(request):
    return render(request,'login.html')
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'index.html',context)