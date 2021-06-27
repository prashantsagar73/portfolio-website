from django.shortcuts import render
from .models import Timeline, Blog

# Create your views here.
def home(request):
    context = {
        'posts': Timeline.objects.all()
    }
    return render(request,'home/index.html',context)

def blog(request):
    contexts = {
        'blogs': Blog.objects.all()
    }
    return render(request,'home/first.html',contexts)

