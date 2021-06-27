from django.urls import include ,path
# from django.views.generic import TemplateView

from . import views
app_name = 'prashant'

urlpatterns = [
    path('',views.home,name="home"),
    path('blog/',views.blog,name="blog"),

    # path("first/", TemplateView.as_view(template_name="home/first.html")),
]
