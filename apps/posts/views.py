from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from apps.posts.models import Post, PostComment, PostLike, PostFavorite
from apps.posts.serializers import PostSerializer, PostDetailSerializer, PostCommentSerializer, PostLikeSerilizer, PostFavoriteSerializer
from apps.posts.permissions import PostPermission

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission, )

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return PostDetailSerializer
        return PostSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class PostCommentAPIViewSet(GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (PostPermission, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class PostLikeAPIViewSet(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerilizer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class PostFavoriteAPIViewSet(GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin):
    queryset = PostFavorite.objects.all()
    serializer_class = PostFavoriteSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)