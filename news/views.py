from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from news.models import NewsItem
from news.serializers import NewsSerializer, AccountSerializer, UserTokenSerializer, TestSerializer
from users.models import Account


class NewsView(ModelViewSet):
    queryset = NewsItem.objects.all().order_by('-date')
    serializer_class = NewsSerializer


class AccountView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [permissions.IsAuthenticated]


class NewsCreateView(CreateAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsSerializer


class UserLogin(APIView):
    serializer_class = UserTokenSerializer

    def post(self, request, format=None):
        """post user request"""
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = Account.objects.get(student_id=serializer.data.get('student_id'))
            if user is not None:
                token, create_or_fetch = Token.objects.get_or_create(
                    user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            msg = 'Wrong credentials. Please try again'
            return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def testView(request):
    objs = NewsItem.objects.all()
    serializer = TestSerializer(objs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def testDetail(request, pk):
    try:
        obj = NewsItem.objects.get(id=pk)
        serializer = TestSerializer(obj, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'object is not found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def testCreate(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


