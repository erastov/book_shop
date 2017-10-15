from book_shop_app.models import Book
import django_filters


class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ['name', 'publishing_house', 'author', 'subject', 'year', 'price']