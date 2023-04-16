from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from camila_sanfuentes_com.models import MainPageContent
from gallery.models import Gallery, GalleryImage
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy


# Create your views here.

class BlogIndex(TemplateView):
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        context['galleries'] = Gallery.objects.all()
        context['carousel_images'] = GalleryImage.objects.filter(carousel_image=True).all()
        return context


class NewPost(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        context['galleries'] = Gallery.objects.all()
        context['carousel_images'] = GalleryImage.objects.filter(carousel_image=True).all()
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        context['galleries'] = Gallery.objects.all()
        context['carousel_images'] = GalleryImage.objects.filter(carousel_image=True).all()
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        context['galleries'] = Gallery.objects.all()
        context['carousel_images'] = GalleryImage.objects.filter(carousel_image=True).all()
        return context


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date__lte=timezone.now()).order_by('-date')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        context['galleries'] = Gallery.objects.all()
        context['carousel_images'] = GalleryImage.objects.filter(carousel_image=True).all()
        return context


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_list')
