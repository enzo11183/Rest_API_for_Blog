from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(editable=False, default=timezone.now)
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        return reverse('BlogApp:blog_detail', args=[self.id])


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comments' )
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comments')

    class Meta:
        ordering = ('-created',)