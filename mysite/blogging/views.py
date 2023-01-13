from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blogging.models import Post


class PostListView(ListView):
    context_object_name = "post_list"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"

class PostDetailView(DetailView):
    context_object_name = "post_detail"
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"

class PostAddView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blogging/add.html"
    fields = ['title', 'text']
    success_url = reverse_lazy("blog_index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = datetime.now()
        return super().form_valid(form)