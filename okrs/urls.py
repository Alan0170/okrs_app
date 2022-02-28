"""okrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from okr.api.views.integrante_view import IntegranteViewSet
from okr.api.views.okr_api_view import OkrViewSet

router = DefaultRouter()
router.register(r'okr_api', OkrViewSet)
router.register(r'okr_integrantes', IntegranteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('okr.urls')),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),

 ]
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
