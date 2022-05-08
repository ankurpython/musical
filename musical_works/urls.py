from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicalView

router = DefaultRouter()
router.register('musical', MusicalView, basename='musical')

urlpatterns = [
    path('', include(router.urls)),
]
