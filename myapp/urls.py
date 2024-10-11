
from django.contrib import admin
from django.urls import path,include
from .views import *
from logging import DEBUG
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
   
   
   path('',home_view),
   path('home/',home_view),
   path('create-blog/', create_blog, name='create_blog'),
   path('update-blog/<int:pk>',update_blog),
   path('delete-blog/<int:pk>',delete_blog),
   path('view-blog/<str:user>',view_blog),
   path('view-by-id/<int:pk>',view_by_id),
   path('register/', register),
   path('login/', login_page),
   path('logout/',logout_page),
   path('profile-update/<int:pk>/',profile_update),
   path('category/',get_category),
   path('get_user',get_user),
   path('upload/', upload_image, name='upload_image'),
   path('blog_by_category/<int:pk>',view_blog_category),
   path('comment/<int:pk>',comment),
   path('like/<int:pk>',like),
   
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)