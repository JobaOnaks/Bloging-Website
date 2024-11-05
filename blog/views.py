from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogListview(ListView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'readblogs.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = "edit_myblogs.html"
    success_url = reverse_lazy('myblog')

class BlogDetailView(DetailView):
    model = Post
    template_name = 'readblog_details.html'
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "deleteblog.html"
    success_url = reverse_lazy('myblog')

class MyBlogListView(ListView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'myblogs.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title','author','body']
    template_name = 'createblog.html'
    success_url = reverse_lazy('myblog')