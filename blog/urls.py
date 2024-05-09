from django.urls import path
from .views import CreatePost

urlpatterns = [
    path('', CreatePost.as_view(), name='create_post'),
]