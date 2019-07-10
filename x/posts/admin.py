from django.contrib import admin
from posts.models import Category
from posts.models import Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)