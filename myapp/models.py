from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    categoryName= models.CharField(max_length=200,null=True,blank =True)
    def __str__(self):
        return self.categoryName
    
class UserImage(AbstractUser):
    image=models.ImageField(upload_to="uploads",null=True)
    def __str__(self):
        return self.username
    
class BlogPost(models.Model):
    user= models.ForeignKey(UserImage,null=True, blank=True, on_delete=models.CASCADE ,related_name="blog_user")
    category=models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE,related_name="blog_category")
    title = models.CharField(max_length=255)
    content = models.TextField()
    image=models.ImageField(null=True,upload_to="uploads")
    
    def __str__(self):
        return self.title
