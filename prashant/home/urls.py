from django.contrib import admin
from django.urls import include ,path
from .views import PostListView, PostDetailView, TimeListView, ImposListView
app_name = 'prashant'

# admin page customization 
admin.site.site_header= "Prashant's Portfolio"
admin.site.site_title= "Welcome to Prashant's portfolio website"
admin.site.index_title= "Welcome to this website"

# urlpatterns of pages 
urlpatterns = [
    path('',TimeListView.as_view(),name="home"),
    path('imposible/',ImposListView.as_view(),name="impos"),
    # path('imposible/',views.impos,name="imposible"),
    path('blog/', PostListView.as_view(), name ="blog"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name ="post_detail"),

]
