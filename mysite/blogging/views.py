from django.shortcuts import render
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post

class PostListView(ListView):
    context_object_name = 'post_list'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    # model = Post
    template_name = 'blogging/list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = ('blogging/detail.html')