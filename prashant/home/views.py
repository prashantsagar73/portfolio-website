from django.db.models.indexes import Index
from django.shortcuts import render
from .models import Timeline, Blog, List
from django.views.generic import ListView, DetailView, detail

# Create your views here.

# home(Index)
def home(request):
    context = {
        'posts': Timeline.objects.all()
    }
    return render(request,'home/index.html',context)

# blog page 
def blog(request):
    contexts = {
        'blogs': Blog.objects.all()
    }
    return render(request,'home/blog.html',contexts)

# blog list 
class PostListView(ListView):
    model = Blog
    template_name = "home/blog.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'blogs'
    ordering =['-timestamp']
    # paginate_by = 9
# blog details
class PostDetailView(DetailView):
    model = Blog
    template_name = 'home/blogpost.html' 

# imposible list 
def impos(request):
    con = {
        'lists': List.objects.all()
    }
    return render(request,'home/imposible.html',con)