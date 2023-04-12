from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Vote, Color, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ColorSerializer(ModelSerializer):
    id = IntegerField(read_only=True)

    class Meta:
        model = Color
        fields = '__all__'


class VoteSerializer(ModelSerializer):
    color = ColorSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'
        depth = 1
