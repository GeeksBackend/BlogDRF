from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, PostCommentAPIViewSet, PostLikeAPIViewSet, PostFavoriteAPIViewSet

router = DefaultRouter()
router.register('posts', PostAPIViewSet, basename='posts')
router.register('comments', PostCommentAPIViewSet, basename='comments')
router.register('likes', PostLikeAPIViewSet, basename='likes')
router.register('favorites', PostFavoriteAPIViewSet, basename='favorites')

urlpatterns = router.urls