from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # Просмотр
    url(r'^(?P<entity>[_a-z]+)/$', views.show),
    # Книги
    url(r'^books/new/$', views.books_new, name='books_new'),
    url(r'^books/(?P<id>\d+)/edit/$', views.books_edit, name='books_edit'),
    # Клиенты
    url(r'^customers/new/$', views.customers_new, name='customers_new'),
    url(r'^customers/(?P<id>\d+)/edit/$', views.customers_edit, name='customers_edit'),
    # Книга
    url(r'^book/(?P<id>\d+)/$', views.book, name='book'),
     # Издавтельство
    url(r'^publishing_houses/new/$', views.publishing_houses_new, name='publishing_houses_new'),
    url(r'^publishing_houses/(?P<id>\d+)/edit/$', views.publishing_houses_edit, name='publishing_houses_edit'),
    # Удаление
    url(r'^(?P<entity>[a-z]+)/delete/(?P<id>\d+)/$', views.delete),
]