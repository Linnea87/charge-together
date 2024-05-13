from django.urls import path
from .views import CreatePost, PostList

urlpatterns = [
    path('create/', CreatePost.as_view(), name='create_post'),
    path('post/', PostList.as_view(), name='post_list')
]