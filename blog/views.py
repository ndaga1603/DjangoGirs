from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post


# Create your views here.

class Homepage(ListView):
    model = Post
    template_name = "home.html"