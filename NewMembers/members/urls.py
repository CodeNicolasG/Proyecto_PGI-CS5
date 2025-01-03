# members/urls.py
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('new/', IndexView, name='new_member'),
]
