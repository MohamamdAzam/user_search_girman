
from django.urls import path
from .views import search_users

urlpatterns = [
    path('api/search/', search_users, name='search_users'),
]


