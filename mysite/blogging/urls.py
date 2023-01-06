from django.urls import path
from blogging.views import list_view, detail_view, stub_view

urlpatterns = [
    path('', stub_view, name="blog_index"),
    path('posts/', list_view, name="blog_list"),
    path('posts/<int:post_id>/', detail_view, name="post_detail"),
]