from django.contrib import admin
from django.db import models
from .models import Timeline, Blog, List

# Register your models here.
admin.site.register((Timeline,List ))


# tiny editior in blog models
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css= {
            "all": ("css/main.css",)
        }
        js = ("js/blog.js",)
admin.site.register(Blog, BlogAdmin)
