from    django.urls import path
from MyApp import views

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view())
]