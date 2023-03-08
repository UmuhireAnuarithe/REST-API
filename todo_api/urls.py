# from django.conf.urls import url
from django.urls import path, include
from .views import  APIlistView


urlpatterns = [
    path('api/', APIlistView.as_view()),
]