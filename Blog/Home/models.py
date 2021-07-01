from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=244)
    content=models.TextField()
    date=models.DateField()
    category=models.CharField(max_length=100,null=True)
    uploader=models.CharField(max_length=100)
    credit=models.CharField(max_length=254)
    image=models.ImageField(upload_to='static/')
    def __str__(self):
        return self.title
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField()
    email=models.EmailField()
    def __str__(self):
        return self.name
class Staff(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.username
