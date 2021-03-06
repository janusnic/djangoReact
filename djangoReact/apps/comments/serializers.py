from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'created_at')
