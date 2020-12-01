from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer
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