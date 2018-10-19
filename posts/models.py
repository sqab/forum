from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CommentPost(models.Model):
    class Meta():
        db_table = 'comments'
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    text = models.TextField("Comment text", max_length=500)
    created = models.DateTimeField("Date", auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField("Like date", auto_now_add=True)


class Hit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField("Hit date", auto_now_add=True)
