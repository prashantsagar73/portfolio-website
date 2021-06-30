from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Timeline(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=500,default=" ")
    content = models.TextField(default=" ")
    timestamp = models.DateField(default=timezone.now)
    link = models.URLField(("Link"), max_length=1000,
        unique=False, 
        blank=True)

    def __str__(self):
        return self.title 

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField(default=" ")
    short_desc = models.CharField(max_length=300,default="")
    timestamp = models.DateField(default=timezone.now)
    link = models.URLField(("Link"), max_length=1000,
        unique=False, 
        blank=True)

    def __str__(self):
        return self.title   

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})         
