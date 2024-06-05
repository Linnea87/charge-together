from django.views.generic import (
    CreateView, ListView, 
    DetailView, DeleteView,
    UpdateView

)
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm



class PostList(ListView):
    """
    view all blog posts
    """
    model = Post
    template_name = "blog/blog.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate comment count for each post
        for post in context['post_list']:
            post.comment_count = post.comments.count()
        return context

class PostLike(DetailView):

    def post(self, request, pk):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


class PostDetail(DetailView):
    """
    Click and open a singel blog post
    """
    template_name = "blog/post_detail.html"
    model = Post
    queryset = Post.objects.order_by("-created_on")
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data
     

class CreatePost(LoginRequiredMixin, CreateView):
    """
    Add Post view
    """
    model = Post
    template_name = "blog/create_post.html"
    form_class = PostForm
    success_url = "/blog/"
    queryset = Post.objects.filter(status=1)

    def form_valid(self, form):
        form.instance.author = self.request.user  
        if form.instance.status == 0:
            messages.success(self.request, 'Your draft are saved')
        else:
            messages.success(self.request, 'Your post are Published!')
        return super(CreatePost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    The User can edit their own existing blog post
    """
    template_name = "blog/edit_post.html"
    model = Post
    success_url = "/blog/"
    form_class = PostForm
    
    def form_valid(self, form):
        messages.success(self.request, 'Your post are updated!')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    The user can delete their own existing blog post
    """
    model = Post
    success_url = "/blog/"

    def form_valid(self, form):
        messages.success(self.request, 'Your post are deleted!')
        return super().form_valid(form)
   
    def test_func(self):
        return self.request.user == self.get_object().author
     

class NewComment(LoginRequiredMixin, CreateView):
    """
    Add Post view
    """
    model = Comment
    template_name = "blog/comment.html"
    form_class = CommentForm
    success_url = "/blog/" 
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        messages.success(self.request, 'Thank you for your comment!')
        return super().form_valid(form)
    

class EditComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit own comment"""

    template_name = "blog/edit_comment.html"
    model = Comment
    success_url = "/blog/"
    form_class = CommentForm
   
    def form_valid(self, form):
        messages.success(self.request, 'Your comment are updated')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user 
    


    




