from django.core.management.base import BaseCommand
from myapp.models import *
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Generate slugs for existing blog posts'

    def handle(self, *args, **kwargs):
        posts =UserImage.objects.all()
        for post in posts:
            if not post.slug:
                post.slug = slugify(post.username)
                post.save()
                self.stdout.write(self.style.SUCCESS(f"Slug generated for: {post.username}"))