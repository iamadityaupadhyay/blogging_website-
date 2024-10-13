from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Category)
# admin.site.register(UserImage)
from .models import *
class UserImageAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image',)}),
    )

admin.site.register(UserImage, UserImageAdmin)
admin.site.register(Comment)
admin.site.register(Like)
from django.utils.html import mark_safe
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')  # To display in the list view
    readonly_fields = ('image_preview',)  # To display in the form view
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 150px; height: 150px;" />')
        return "No image uploaded"
    
    image_preview.short_description = 'Image Preview'

admin.site.register(BlogPost, BlogPostAdmin)