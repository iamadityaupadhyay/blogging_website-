from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
class Category(models.Model):
    categoryName= models.CharField(max_length=200,null=True,blank =True)
    def __str__(self):
        return self.categoryName
    
class UserImage(AbstractUser):
    image = CloudinaryField('image', blank=True, null=True)
    def __str__(self):
        return self.username
    
class BlogPost(models.Model):
    user= models.ForeignKey(UserImage,null=True, blank=True, on_delete=models.CASCADE ,related_name="blog_user")
    category=models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE,related_name="blog_category")
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = CloudinaryField('image', blank=True, null=True)
    def __str__(self):
        return self.title
