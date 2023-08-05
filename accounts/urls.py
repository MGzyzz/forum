from django.urls import path
from accounts import views


urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('users/<int:id>/detail/', views.Detail.as_view(), name='user_detail'),
]
