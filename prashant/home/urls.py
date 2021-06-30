from django.urls import include ,path
from .views import PostListView, PostDetailView 
# from django.views.generic import TemplateView

from . import views
app_name = 'prashant'

urlpatterns = [
    path('',views.home,name="home"),
    path('imposible/',views.impos,name="imposible"),
    path('blog/', PostListView.as_view(), name ="blog"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name ="post_detail"),

]
