from django.contrib.auth.models import User
from django.db import models as m
from django.utils import timezone


class Tag(m.Model):
    name = m.CharField(max_length=15)
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)
    active = m.BooleanField(default=True)

    def __str__(self):
        return f'Tag {self.name}'


class Post(m.Model):
    class Status(m.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = m.CharField(max_length=250)
    slug = m.SlugField(max_length=250, unique_for_date='publish')
    author = m.ForeignKey(User, on_delete=m.CASCADE, related_name='posts')
    status = m.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    body = m.TextField()
    tags = m.ManyToManyField(Tag, related_name='posts')
    publish = m.DateTimeField(default=timezone.now)
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(m.Model):
    post = m.ForeignKey(Post, on_delete=m.CASCADE, related_name='comments')
    user = m.ForeignKey(User, on_delete=m.CASCADE, related_name='comments')
    email = m.EmailField()
    body = m.TextField()
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)
    active = m.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'


class Contact(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE, related_name='contact')
    phone = m.CharField(max_length=10)
    email = m.EmailField()
    address = m.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} tel. {self.phone}'