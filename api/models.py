from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User,
        related_name='messages',
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.timestamp}: Message{self.id} {self.text} from user:{self.user}'


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.timestamp}: Comment{self.id} {self.text} from user {self.user}'
