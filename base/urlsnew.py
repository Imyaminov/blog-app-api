from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostAPIView)
    # path('', views.PostAPIView)
]