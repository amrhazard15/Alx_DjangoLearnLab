from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
     path('', views.home),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('notifications.urls')),

    # Schema and Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


