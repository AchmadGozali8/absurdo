from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

from .models import Posts, Comments, Likes, Alarams
from .serializers import (UserSerializer, PostsSerializer, LikesSerializer,
                          CommentsSerializer, AlaramsSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    filter_fields = ('title',)


class LikesViewSet(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class AlaramsViewSet(ModelViewSet):
    queryset = Alarams.objects.all()
    serializer_class = AlaramsSerializer
