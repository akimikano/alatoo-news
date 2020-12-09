from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from news.models import NewsItem
from users.models import Account


class NewsSerializer(ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['student_id', 'name_surname']


class UserTokenSerializer(serializers.Serializer):
    student_id = serializers.CharField(required=True)


class TestSerializer(ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'


