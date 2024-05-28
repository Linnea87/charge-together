from django.db import models
from blog.models import Post
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField



class Profile(models.Model):
    """
    Model for the Profile
    """

    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to="profiles/",
        force_format="WEBP",
        blank=False,
    )
    bio = RichTextField(max_length=2500, null=True, blank=True)
    liked_post = models.ManyToManyField(Post, related_name="liked_post", blank=True)
    
    def __str__(self):
        return str(self.user.username)

class PostLike(models.Model):
    """ Model representing a like for a specific post by a user. Code used from the Code Institute's I think, Therefore I blog. """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """
    The user can create and update the profile
    """
    if created:
        Profile.objects.create(user=instance)
