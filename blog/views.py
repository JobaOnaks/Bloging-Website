from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post,Comment
from .forms import NewPost,EditPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogListview(ListView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'readblogs.html'
    ordering = ['-date']
    login_url = 'login'

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = EditPost
    template_name = "edit_myblogs.html"
    success_url = reverse_lazy('myblog')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDetailView(DetailView):
    model = Post
    template_name = 'readblog_details.html'
    
class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "deleteblog.html"
    success_url = reverse_lazy('myblog')
    login_url = 'login'

class MyBlogListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'myblogs.html'
    ordering = ['-date']
    login_url = 'login'

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # form_class = NewPost
    template_name = 'createblog.html'
    success_url = reverse_lazy('myblog')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ('name','body')

    def form_valid(self, form):
        post_uuid = self.kwargs["pk"]
        post = Post.objects.filter(uuid=post_uuid).first()
        form.instance.post = post
        return super().form_valid(form)
    
    success_url = reverse_lazy('readblog')
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__icontains=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})