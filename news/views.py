from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from news.models import NewsItem
from news.serializers import NewsSerializer, AccountSerializer
from users.models import Account


class NewsView(ModelViewSet):
    queryset = NewsItem.objects.all().order_by('-date')
    serializer_class = NewsSerializer


class AccountView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class NewsCreateView(CreateAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsSerializer


def base(request):
    return HttpResponse('It is base page')


