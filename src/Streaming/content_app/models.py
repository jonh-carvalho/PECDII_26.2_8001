from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CONTENT_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='published')
    creator = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.ForeignKey(Content, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.content.title}'


class Like(models.Model):
    content = models.ForeignKey(Content, related_name='likes_set', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('content', 'user')

    def __str__(self):
        return f'Like by {self.user.username} on {self.content.title}'

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    # A playlist is a collection of content items
    # A user can have multiple playlists, and a playlist can contain multiple content items.
    user = models.ForeignKey(User, related_name='playlists', on_delete=models.CASCADE)
    # A playlist can contain multiple content items, and a content item can belong to multiple playlists.
    contents = models.ManyToManyField(Content, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Playlist: {self.name} by {self.user.username}'