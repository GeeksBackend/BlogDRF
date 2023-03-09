from django.contrib import admin

from apps.posts.models import Post, PostComment, PostLike, PostFavorite

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'created')
    search_fields = ('user__username', 'title', )
    list_filter = ('user', 'title')
    list_per_page = 5

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'created')
    search_fields = ('post__title', 'user__username', 'text', 'created')
    list_filter = ('post', 'user', 'text', 'created')
    list_per_page = 20

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user__username')
    list_filter = ('post', 'user')
    list_per_page = 30

class PostFavoriteAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user__username')
    list_filter = ('post', 'user')
    list_per_page = 30

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(PostFavorite, PostFavoriteAdmin)