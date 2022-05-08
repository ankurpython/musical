import django_filters
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import MusicalMetadata
from .serializers import MusicalSerializer
from django_filters import rest_framework as filter


class Filters(django_filters.FilterSet):
    contributors = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = MusicalMetadata
        fields = ['title', 'contributors', 'iswc']


class MusicalView(viewsets.ModelViewSet):
    serializer_class = MusicalSerializer
    queryset = MusicalMetadata.objects.all()

    filter_backends = [filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = Filters
    search_fields = ['title', 'contributors', 'iswc']
    ordering_fields = ['title', 'iswc']