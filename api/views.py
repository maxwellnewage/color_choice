from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Vote, Color
from .serializers import ColorSerializer, VoteSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from utils.fake_user_generator import fake_users


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = VoteSerializer(data=request.data)

        if serializer.is_valid():
            color = Color(**request.data['color'])

            serializer.save(user=request.user, color=color)
            return Response({
                "success": True,
                "message": "Voto emitido exitosamente.",
                "vote": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "success": False,
                "message": "Error al emitir Voto!",
                "vote": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_auth(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Se debe indicar usuario y contraseña'}, status=status.HTTP_204_NO_CONTENT)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response({'error': 'El usuario o la contraseña son incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def is_voted(request):
    vote = Vote.objects.filter(user=request.user).first()

    if vote is None:
        return Response({
            "is_voted": False,
            "message": f"{request.user} no ha votado.",
        })
    else:
        return Response({
            "is_voted": True,
            "message": f"{request.user} ya ha votado el color {vote.color}.",
        })


# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def votes_stats(request):
#     votes =
#     votes_by_color = Vote.objects.values('color__name')
#     result = {}
#     for vote in votes_by_color:
#         result[vote['color__name']] = vote['count']
#     return result

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def generate_fake_users(request, amount):
    user_list = fake_users(amount)
    user_serializer_list = [UserSerializer(user).data for user in user_list]

    return Response({"users": user_serializer_list})
