from rest_framework import serializers
from .models import TastingNote, Comment


class TastingNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TastingNote
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'