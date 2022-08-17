from rest_framework import serializers
from api_basic.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    blog_posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'is_superuser', 'blog_posts']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'body', 'author', 'publish']


