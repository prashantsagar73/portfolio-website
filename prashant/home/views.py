from django.shortcuts import render
from .models import Timeline, Blog
from django.views.generic import ListView, DetailView

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
    return render(request,'home/blog.html',contexts)

class PostListView(ListView):
    model = Blog
    template_name = "home/blog.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'blogs'
    ordering =['-timestamp']
    # paginate_by = 9

class PostDetailView(DetailView):
    model = Blog
    template_name = 'home/blogpost.html' 

# imposible list 
def impos(request):
    return render(request,'home/imposible.html')