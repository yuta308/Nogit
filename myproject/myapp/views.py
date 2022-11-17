from multiprocessing import context
from django.shortcuts import render,resolve_url
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView
from .models import Post
from django.urls import reverse_lazy
from .form import PostForm
from django.views.generic import TemplateView,CreateView,DetailView,UpdateView,DeleteView


class Index(TemplateView):
    template_name='myapp/index.html'

    def get_context_data(self,*args, **kwargs) :
        context = super().get_context_data
        post_list= Post.objects.all().order_by('-created_at')
        context={'post_list':post_list,}
        return context


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('myapp:index')


class PostDetail (DetailView):
    model=Post


class PostUpdate(UpdateView):
    model=Post
    form_class =PostForm
    def get_success_url(self):
        return resolve_url('myapp:post_detail',pk=self.kwargs['pk'])

class PostDelete(DeleteView):
    model=Post
    def get_success_url(self):
        return resolve_url('myapp:index')