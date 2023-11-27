from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes, name = 'getRoutes'),
    path('token/', MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name = 'token_refresh'),
    path('signin/', views.signin, name = 'signin'),
    path('flash/<str:pk>/', views.getFlash, name = 'getFlash'),
    path('flashpack/<str:pk>/', views.flashCards, name = 'flashCards'),
    path('createflash/', views.createFlash, name = 'createFlash'),
    path('createcard/', views.createCard, name = 'createCard')
]