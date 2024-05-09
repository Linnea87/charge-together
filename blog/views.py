from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

class CreatePost(LoginRequiredMixin, CreateView):
    """
    Add Post view
    """
    template_name = 'blog/create_post.html'
    model= Post
    form_class = PostForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)

