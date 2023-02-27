from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.Response):
    queryset = Post.objects.all()
    serializer_class = PostSerializer