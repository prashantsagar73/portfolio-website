from django.contrib import admin
from django.urls import include ,path
from .views import PostListView, PostDetailView 
from . import views
app_name = 'prashant'

admin.site.site_header= "Prashant's Portfolio"
admin.site.site_title= "Welcome to Prashant's portfolio website"
admin.site.index_title= "Welcome to this website"

urlpatterns = [
    path('',views.home,name="home"),
    path('imposible/',views.impos,name="imposible"),
    path('blog/', PostListView.as_view(), name ="blog"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name ="post_detail"),

]
