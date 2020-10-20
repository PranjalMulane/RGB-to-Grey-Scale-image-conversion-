from django.urls import path, include
from .views import recognise 


urlpatterns = [
    path('',recognise)
]
