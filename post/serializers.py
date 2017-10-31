from django.contrib.auth.models import User
from .models import Posts, Comments, Likes, Alarams
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'last_login')


class PostsSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Posts
        exclude = ('deleted', 'updated_at', 'deleted_at', 'created_at')


class CommentsSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Comments
        exclude = ('deleted', 'updated_at', 'deleted_at', 'created_at')



class LikesSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Likes
        exclude = ('updated_at', 'deleted_at', 'created_at')


class AlaramsSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Alarams
        exclude = ('updated_at', 'deleted_at', 'created_at')
