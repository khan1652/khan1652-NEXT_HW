from django.db import models
from accounts.models import Profile


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="my_posts", null=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="my_comments", null=True
    )

    def __str__(self):
        return self.content
