from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
admin.site.register(BlogPost)
admin.site.register(Category)
# admin.site.register(UserImage)

class UserImageAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image',)}),
    )

admin.site.register(UserImage, UserImageAdmin)