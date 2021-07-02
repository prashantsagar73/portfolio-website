from django.shortcuts import render
from .models import Timeline, Blog, List
from django.views.generic import ListView, DetailView


# Create your views here.

# home(Index)
class TimeListView(ListView):
    model = Timeline
    template_name = "home/index.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'posts'
    ordering =['-timestamp']

# blog list 
class PostListView(ListView):
    model = Blog
    template_name = "home/blog.html"  
    context_object_name = 'blogs'
    ordering =['-timestamp']
    # paginate_by = 9

# blog details
class PostDetailView(DetailView):
    model = Blog
    template_name = 'home/blogpost.html' 


# imposible list 
class ImposListView(ListView):
    model = List
    template_name = "home/imposible.html" 
    context_object_name = 'lists'
# def impos(request):
#     con = {
#         'lists': List.objects.all()
#     }
#     return render(request,'home/imposible.html',con)