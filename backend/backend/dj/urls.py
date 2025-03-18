"""
URL configuration for dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from backend.dj.app import models

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cat
        fields = ["name"]

class CatViewSet(viewsets.ModelViewSet):
    queryset = models.Cat.objects.all()
    serializer_class = CatSerializer

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)

class MyLoginView(auth_views.LoginView):
    success_url_allowed_hosts = {settings.FRONTEND_URL.replace("http://", "")}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("backend.dj.app.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path("accounts/login/", MyLoginView.as_view(), name="login"),
]
