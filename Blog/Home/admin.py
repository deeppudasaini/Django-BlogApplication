from django.contrib import admin
from .models import Post,Feedback,Staff
# Register your models here.
admin.site.register(Post)
admin.site.register(Feedback)
admin.site.register(Staff)