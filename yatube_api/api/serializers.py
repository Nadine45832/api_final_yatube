from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username', required=True,
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = serializers.StringRelatedField(label='image', required=False)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, default=serializers.CurrentUserDefault(),
        slug_field='username')
    post = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
