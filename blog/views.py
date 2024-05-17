from django.views.generic import (
    CreateView, ListView, 
    DetailView, DeleteView,
    UpdateView

)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class PostList(ListView):
    """
    view all blog posts
    """
    model = Post
    template_name = "blog/blog.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")


class PostDetail(DetailView):
    """
    Click and open a singel blog post
    """
    template_name = "blog/post_detail.html"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")


class CreatePost(LoginRequiredMixin, CreateView):
    """
    Add Post view
    """
    model = Post
    template_name = "blog/create_post.html"
    form_class = PostForm
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)
    

class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    The User can edit their own existing blog post
    """
    template_name = "blog/edit_post.html"
    model = Post
    success_url = "/blog/"
    form_class = PostForm
    
    def test_func(self):
        return self.request.user == self.get_object().author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    The user can delete their own existing blog post
    """
    model = Post
    success_url = "/blog/"
    
    def test_func(self):
        return self.request.user == self.get_object().author