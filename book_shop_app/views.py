from django.shortcuts import render
import sqlite3
from django.http import HttpResponseRedirect
from book_shop_app.models import Customer, Employee, Order, PublishingHouse, Comment, Book, MoreAboutOrder
from .forms import CustomerForm, BookForm, PublishingHouseForm
from django.shortcuts import get_object_or_404
from .filters import BookFilter


def customers_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/customers/')
    else:
        form = CustomerForm()
    return render(request, 'book_shop_app/customers_new_edit.html', {'form': form})


def customers_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/customers/')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'book_shop_app/customers_new_edit.html', {'form': form})


def publishing_houses_new(request):
    if request.method == "POST":
        form = PublishingHouseForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/publishing_houses/')
    else:
        form = AccessoryForm()
    return render(request, 'book_shop_app/publishing_house_new_edit.html', {'form': form})


def publishing_houses_edit(request, id):
    publishing_house = get_object_or_404(PublishingHouse, id=id)
    if request.method == "POST":
        form = PublishingHouseForm(request.POST, instance=publishing_house)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/publishing_houses/')
    else:
        form = PublishingHouseForm(instance=publishing_house)
    return render(request, 'book_shop_app/publishing_house_new_edit.html', {'form': form})


def books_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/books/')
    else:
        form = BookForm()
    return render(request, 'book_shop_app/books_new_edit.html', {'form': form})


def books_edit(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST or None, request.FILES or None, instance=book)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/books/')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_shop_app/books_new_edit.html', {'form': form})


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def index(request):
    """Домашняя страница"""
    books = Book.objects.all()
    books_filter = BookFilter(request.GET, queryset=books)
    context = {'values': books_filter}
    return render(request, 'book_shop_app/index.html', context)


def book(request, id):
    """Домашняя страница"""
    book = get_object_or_404(Book, id=id)
    comments = Comment.objects.filter(book=book)
    context = {'book': book, 'comments': comments}
    return render(request, 'book_shop_app/book.html', context)


def show(request, entity):
    """Просмотр"""
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = dict_factory
    cursor = con.cursor()

    templates = {
            'customers': 'book_shop_app/customers.html',
            'books': 'book_shop_app/books.html',
            'publishing_houses': 'book_shop_app/publishing_houses.html'
            }

    sql = {
            'customers': ("SELECT * FROM book_shop_app_customer"),
            'books': ("SELECT a.id as id, a.name as name, author, b.name as publishing_house, year, price, count, subject "
                      "FROM book_shop_app_book a "
                      "INNER JOIN book_shop_app_publishinghouse b ON a.publishing_house_id = b.id "),
            'publishing_houses': ("SELECT * FROM book_shop_app_publishinghouse"),
            }

    cursor.execute(sql[entity])
    rows = cursor.fetchall()
    context = {'values': rows}
    
    return render(request, templates[entity], context)


def delete(request, id, entity):
    """Удаление сотрудника"""
    con = sqlite3.connect("db.sqlite3")
    con.row_factory = dict_factory
    cursor = con.cursor()

    sql = {'books': ("DELETE "
                       "FROM book_shop_app_book "
                       "WHERE id = " + str(id)),
            'customers': ("DELETE "
                          "FROM book_shop_app_customer "
                          "WHERE id = " + str(id)),
            'publishing_houses': ("DELETE "
                          "FROM book_shop_app_publishinghouse "
                          "WHERE id = " + str(id)),
            }
    cursor.execute(sql[entity])

    con.commit()
    return HttpResponseRedirect('/' + entity)