from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime, date
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    category = models.CharField(max_length=255)

class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    body = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='life')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    comments = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)