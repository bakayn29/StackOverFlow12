from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplaySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


