from django.shortcuts import render,HttpResponse

# Create your views here.
def Index(request):
    return render(request,'index.html')
def About(request):
    return render(request,'about.html')    
def Contact(request):
    return render(request,'contact.html')
def SinglePost(request):
    return render(request,'post.html')
def Login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'index.html')