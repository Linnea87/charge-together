from django.urls import path
from .views import (
    CreatePost, PostList, 
    PostDetail, DeletePost,
    EditPost, PostLike, NewComment
)

urlpatterns = [
    path("create/", CreatePost.as_view(), name="create_post"),
    path("", PostList.as_view(), name="post_list"),
    path("<slug:pk>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:pk>/", DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:pk>/", EditPost.as_view(), name="edit_post"),
    path("like/<int:pk>", PostLike.as_view(), name="post_like"),
    path("<int:pk>/comment/", NewComment.as_view(), name="new_comment"),
    # path("<int:pk>/edit", EditComment.as_view(), name="edit_comment"),
  
]
