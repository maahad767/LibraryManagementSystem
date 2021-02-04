from django.db.models import Q
import django_filters

from .models import *


class BookFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter')

    class Meta:
        model = Book
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Book.objects.filter(
            Q(title__icontains=value) | Q(author__name__icontains=value) | Q(publisher__name__icontains=value)
        )