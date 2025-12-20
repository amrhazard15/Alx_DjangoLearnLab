from django.urls import path
from django.http import HttpResponse
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to Accounts API"), name='accounts-home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
