from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy


# Create your views here.

class BlogIndex(TemplateView):
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    model = Post


class NewPost(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date__lte=timezone.now()).order_by('-date')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_list')
