from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from .views import RegisterAPI, LoginAPI


urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist')
]

