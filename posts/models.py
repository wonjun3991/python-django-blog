from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return Post.title

class Comment(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
