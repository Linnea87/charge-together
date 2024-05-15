from django.views.generic import CreateView, ListView, DetailView
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
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)
