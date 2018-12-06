"""k9service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from breeds.views import BreedCreateView, BreedRUDView
from dogs.views import DogCreateView, DogRUDView

urlpatterns = [
    path('breed/', BreedCreateView.as_view()),
    path('breed/<uuid:pk>/', BreedRUDView.as_view()),
    path('dog/', DogCreateView.as_view()),
    path('dog/<uuid:pk>/', DogRUDView.as_view()),
]
