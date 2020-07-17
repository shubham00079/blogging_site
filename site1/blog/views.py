from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                CreateView,DeleteView,UpdateView)
from blog.models import Post
from blog.forms import PostForm,UpdateForm
from django.urls import reverse_lazy
from django.utils import timezone
# Create your views here.

class About(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post

class PostDraftView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    form_class = UpdateForm
    model = Post


#######################################3

def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
