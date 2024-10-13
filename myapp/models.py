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
    bio=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.username
    
class BlogPost(models.Model):
    user= models.ForeignKey(UserImage,null=True, blank=True, on_delete=models.CASCADE ,related_name="blog_user")
    category=models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE,related_name="blog_category")
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    comment= models.TextField()
    user = models.ForeignKey(UserImage,on_delete=models.CASCADE ,related_name="user_comment",null =True, blank=True)
    blog = models.ForeignKey(BlogPost,on_delete=models.CASCADE ,related_name="blog_comment",null =True, blank=True)
    created_at =models.DateTimeField(auto_now_add=True,null=True,blank =True)
    def __str__(self):
        return self.blog.title
class Like(models.Model):
    like=models.BooleanField(default=False)
    likecount=models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(UserImage,on_delete=models.CASCADE ,related_name="user_like",null =True, blank=True)
    blog=models.ForeignKey(BlogPost,on_delete=models.CASCADE ,related_name="blog_like",null =True, blank=True)
    def __str__(self):
        return self.blog.title