from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, PostCommentAPIViewSet

router = DefaultRouter()
router.register('posts', PostAPIViewSet, basename='posts')
router.register('comments', PostCommentAPIViewSet, basename='comments')

urlpatterns = router.urls