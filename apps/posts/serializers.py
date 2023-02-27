from rest_framework import serializers

from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id', 'user', 'title',
                  'description', 'image', 'created')