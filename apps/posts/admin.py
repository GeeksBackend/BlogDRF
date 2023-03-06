from django.contrib import admin

from apps.posts.models import Post, PostComment, PostLike, PostFavorite

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(PostFavorite)