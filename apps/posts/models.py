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
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class PostComment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="post_comments",
        verbose_name="Пост"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_comments",
        verbose_name="Пользователь"
    )
    text = models.CharField(
        max_length=300,
        verbose_name="Комментарий"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания комментария"
    )

    def __str__(self):
        return f"{self.post} {self.user}"
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class PostLike(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_likes_post"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes_post"
    )

    def __str__(self):
        return f"{self.user} {self.post}"
    
    class Meta:
        verbose_name = "Лайк к посту"
        verbose_name_plural = "Лайки к постам"

class PostFavorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_favorites"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="posts_favorites"
    )

    def __str__(self):
        return f"{self.user} {self.post}"
    
    class Meta:
        verbose_name = "Избранное поста"
        verbose_name_plural = "Избранные постов"