from rest_framework.serializers import ModelSerializer
from .models import Vote, Color


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        depth = 1
