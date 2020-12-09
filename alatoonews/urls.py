"""alatoonews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from news.views import NewsView, AccountView, UserLogin, testView, testDetail, testCreate

router = SimpleRouter()
router.register('api/news', NewsView)
router.register('api/users', AccountView)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', UserLogin.as_view(), name='login'),
    path('api/test/', testView, name='test'),
    path('api/test-detail/<int:pk>', testDetail, name='test-detail'),
    path('api/test-create/', testCreate, name='test-create')
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)