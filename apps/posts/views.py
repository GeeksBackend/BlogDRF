from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from apps.posts.models import Post, PostComment
from apps.posts.serializers import PostSerializer, PostDetailSerializer, PostCommentSerializer

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return PostDetailSerializer
        return PostSerializer

class PostCommentAPIViewSet(GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer