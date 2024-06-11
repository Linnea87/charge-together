from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from autoslug import AutoSlugField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    A model to create and manage blog posts
    """

    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    author = models.ForeignKey(
        User, related_name="post_owner", on_delete=models.CASCADE
    )
    image = ResizedImageField(
        size=[640, 480],
        crop=['middle', 'center'],
        quality=75,
        upload_to="blog/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    excerpt = models.TextField()
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.title)

    def number_of_likes(self):
        return self.likes.count()


class PostLike(models.Model):
    """
    Model representing a like for a specific post by a user. 
    Code used from the Code Institute's I think, Therefore I blog.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Model for leaving comments
    """
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="commenter", on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for the Comment model."""

        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"
