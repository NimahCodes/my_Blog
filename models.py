from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreateBlog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=False,max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
