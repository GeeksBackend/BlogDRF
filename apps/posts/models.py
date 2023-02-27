from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_posts",
        verbose_name="Пользователь поста"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название поста"
    )
    description = models.TextField(
        verbose_name="Описание поста"
    )
    image = models.ImageField(
        upload_to="post_images/",
        verbose_name="Фотография поста"
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"User: {self.user}, Title: {self.title} - {self.created}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"