from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
# Post model
class Post(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='authors' # allows reverse lookup like author.posts.all()
    )
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Comment model:
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE, 
        related_name='comments'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name='comments'
        )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
      return f"Comment by {self.author} on {self.post.title}"
    
# Like Model:
class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE, 
        related_name='likes'
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name='likes'
        )

    def __str__(self):
      return f"Liked by {self.author} on {self.post.title}"