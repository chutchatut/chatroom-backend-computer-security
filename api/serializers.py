from rest_framework import serializers
from .models import Comment, Post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(
        source='user.username'
    )
    class Meta:
        model = Comment
        fields = ('id', 'username', 'timestamp', 'text')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(
        source='user.username'
    )
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'username', 'timestamp', 'text', 'comments')
