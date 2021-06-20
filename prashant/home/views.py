from django.shortcuts import render
from .models import Timeline

# Create your views here.
def home(request):
    context = {
        'posts': Timeline.objects.all()
    }
    return render(request,'home/index.html',context)

def about(request):
    return render(request,'home/first.html')

