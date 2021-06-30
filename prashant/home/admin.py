from django.contrib import admin
from .models import Timeline, Blog

# Register your models here.
admin.site.register(Timeline)


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css= {
            "all": ("css/main.css",)
        }
        js = ("js/blog.js",)
admin.site.register(Blog, BlogAdmin)
