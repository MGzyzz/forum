from django.urls import path
from forum import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:id>/detail', views.DetailTheme.as_view(), name='detail'),
    path('add', views.AddTheme.as_view(), name='add'),
    path('<int:id>/comments', views.UploadComments.as_view(), name='comment')
]