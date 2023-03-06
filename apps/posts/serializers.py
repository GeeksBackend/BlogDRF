from rest_framework import serializers

from apps.posts.models import Post, PostComment, PostLike, PostFavorite


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id', 'user', 'title',
                  'description', 'image', 'created')
        
class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ('id', 'post', 'user', 'text', 'created')

class PostLikeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('id', 'post', 'user')
    
class PostFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFavorite
        fields = ('id', 'post', 'user')

class PostDetailSerializer(serializers.ModelSerializer):
    post_comments = PostCommentSerializer(read_only=True, many=True)
    likes_post = PostLikeSerilizer(read_only=True, many=True)
    class Meta:
        model = Post 
        fields = ('id', 'user', 'title',
                  'description', 'image', 'created', 
                  'post_comments', 'likes_post')
