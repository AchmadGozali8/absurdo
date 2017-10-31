from rest_framework.routers import DefaultRouter

from .api import (UserViewSet, PostsViewSet, LikesViewSet, CommentsViewSet, 
				AlaramsViewSet)

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostsViewSet)
router.register(r'like', LikesViewSet)
router.register(r'comment', CommentsViewSet)
router.register(r'alaram', AlaramsViewSet)
