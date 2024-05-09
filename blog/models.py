from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django_resized import ResizedImageField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    A model to create and manage blog posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    author = models.ForeignKey(User, related_name='post_owner', on_delete=models.CASCADE)
    image = ResizedImageField(
        size =[400, None], quality=75, upload_to='blog/', force_format='WEBP', blank=False, null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    excerpt = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.title)
