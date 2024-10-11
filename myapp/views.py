from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.serializer import *
from django.contrib.auth.decorators import login_required
import html


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        image = request.FILES['upload']
        image_path = default_storage.save(f'uploads/{image.name}', image)
        image_url = f'/media/{image_path}'
        return JsonResponse({'uploaded': True, 'url': image_url})
    
    return JsonResponse({'uploaded': False})

@api_view()
def get_user(request):
    user=UserImage.objects.all()
    serializer = UserSerializer(user,many=True)
    return Response(
        serializer.data
    )
@login_required(login_url="/blog/login")
def create_blog(request):
    if request.method == 'POST':
        data=request.POST
        category=data.get('category')
        content = data.get('content')
        print(f'Category id is {category}')
        title=data.get('title')
        print(f'{html.escape(content)}')
        try:
          image=request.FILES['image']
        except:
          image=None
        try:
            category_object= Category.objects.get(id=category)
            print(category_object)
        except Category.DoesNotExist:
            return render(request,'create_blog_post.html',{"error":"Select a category"})
        
        blog_post = BlogPost.objects.create(
            title=title, 
            content=content,
            category=category_object,
            user=request.user,
            image=image
        )
        return redirect('/blog/home/')
    return render(request, 'create_blog_post.html')

@login_required(login_url="/blog/login")
def view_blog(request,user):
    blog= BlogPost.objects.filter(user=user)
    print(blog)
    context={
       "blogs":blog
    }
    return render(request,"view_blog.html",context)

def view_by_id(request,pk):
    queryset = BlogPost.objects.get(id=pk)
    context ={
        "blog":queryset
    }
    print(context)
    return render(request,"view_more.html",context)

def view_blog_category(request,pk):
    category= Category.objects.get(id=pk)
    print(category)
    blog= BlogPost.objects.filter(category=category)
    context={
        "blogs":blog
    }
    return render(request, "view_blog.html",context)

# Register and login 
def register(request):
    if request.method=="POST":
        data= request.POST
        first_name= data.get("first_name")
        last_name= data.get("last_name")
        username=data.get("username")
        password=data.get("password")
        if UserImage.objects.filter(username=username).exists():
            messages.warning(request, "This is already exists")
            return redirect("/blog/register")
        user= UserImage.objects.create(
            last_name=last_name,
            first_name=first_name,
            username=username,
            email="uaditya219@gmail.com"
        )
        user.set_password(password)
        user.save()
        return redirect("/blog/login/")
    return render(request,"register.html")
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/blog/home/')
    if request.method =="POST":
        data=request.POST
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            # messages.warning(request,"Something went wrong")
            return redirect("/blog/login/")
        login(request,user)
        request.session['just_logged_in']=True
        return redirect("/blog/home/")
    return render(request,"login.html")
def home_view(request):
    blog= BlogPost.objects.all()
    just_logged_in = request.session.pop('just_logged_in', False)
    context={
       "blogs":blog,
       'just_logged_in':just_logged_in
    }
   
    return render(request, 'home.html',context)
def logout_page(request):
        logout(request)
        return redirect("/blog/home/")
    

@api_view()      
def get_category(request):
    try:
        category= Category.objects.all()
    except Category.DoesNotExist:
        raise ValueError
    serializer = CategorySerializer(category,many=True)
    return Response(
            {"Message":"Here is all the category",
             "data":serializer.data}
    )
    

def profile_update(request,pk):
    
    try:
         image= request.FILES['image']
         print(image)
    except:
            image=None 
    user = UserImage.objects.get(id=pk)
    if request.method=="POST":
        # fetching data
        data= request.POST
        first_name= data.get("first_name")
        last_name= data.get("last_name")
        username=data.get("username")
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.image=image
        # user.set_password(password)
        user.save()
        return redirect("/blog/login")
    context={
        "user":user
    }    
    return render(request,"profile_update.html",context)   

@login_required(login_url="/blog/login")
def update_blog(request,pk):
    blog = BlogPost.objects.get(id=pk)
    if request.user!=blog.user:
        return redirect("/blog/home/")
    if request.method =="POST":
        data=request.POST
        title=data.get('title')
        content=data.get('content')
        print(content)
        category=data.get('category')
        try:
            category_object=Category.objects.get(id=category)
            print(category_object)
        except Category.DoesNotExist:
            return render(request,'create_blog_post.html',{"error":"Select a category"})
        
        if title:
            blog.title=title
        if content:
            blog.content=content
        if category:
            blog.category=category_object
        
        try:
            image=request.FILES['image']
        except:image=None
        if image is not None:
            blog.image=image 
        blog.save()
        return redirect("/blog/home/")
  
    context ={
        "blog":blog,
    }
    
    print(context)
    return render(request,"update_blog.html",context)
# delete blog 
@login_required(login_url="/blog/login")
def delete_blog(request,pk):
    blog = BlogPost.objects.filter(id =pk)
    blog.delete()
    return redirect("/blog/home/")