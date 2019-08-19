from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from Blog_Project import settings
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='post_pics')
    # url = models.SlugField(max_length=200, unique=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('Blog_App:post_detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, *kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Blog_App.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('Blog_App:post_list')

    def __str__(self):
        return self.text

# class Reply(models.Model):
#     comment = models.ForeignKey('Blog_App.Comment', on_delete=models.CASCADE, related_name='replies')
#     author = models.CharField(max_length=50)
#     text = models.TextField()
#     time = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.text
#     def Meta():
#         ordering = ('time')
