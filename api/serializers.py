from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Vote, Color, User


class ColorSerializer(ModelSerializer):
    id = IntegerField()

    class Meta:
        model = Color
        fields = '__all__'


class VoteSerializer(ModelSerializer):
    color = ColorSerializer(many=False, read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'
        depth = 1
