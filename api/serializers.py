from rest_framework.serializers import ModelSerializer
from .models import Vote, Color


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        depth = 1
