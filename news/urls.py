from django.urls import path
from news.views import base

urlpatterns = [
    path('', base)
]