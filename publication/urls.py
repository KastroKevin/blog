from django.urls import path
from .views import PostList, PostCreate, CommentCreate, SeachPost


urlpatterns = [
    path('post/', PostList.as_view(), name='post_index'),
    path('post/new', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>', CommentCreate.as_view(), name='post_details'),
    path('post/search/', SeachPost.as_view(), name='search'),
]