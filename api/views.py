from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from .models import Vote, Color
from .serializers import ColorSerializer, VoteSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
