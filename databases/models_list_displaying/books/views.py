from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from books.models import Book

def index(request):
    return redirect(reverse(books_view))

def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.all()
    if pub_date:
        print(f'pub_date={pub_date}, {type(pub_date)}')

        ' Делаем собственный пагинатор '
        pub_dates = map(lambda book: book.pub_date, books)   # Получаем перечень дат выхода книг
        pub_dates = set(pub_dates)  # отсекаем все дублирующиеся записи
        pub_dates = sorted(pub_dates)   # сортируем даты выхода книг в хроногологическом порядке
        prev_page, next_page = None, None

        books = filter(lambda book: book.pub_date == pub_date, books)

    books = list(books)
    print(books, type(books))
    context = {'books': books}
    return render(request, template, context)


def books_pagination_view(request, pub_date):
    template = 'books/books_list.html'
    books = Book.objects.all()
    books = sorted(books, key=lambda item: item.pub_date)
    books = list(books)
    print(f'pub_date={pub_date}, {type(pub_date)}')

    paginator = Paginator(books, 1)
    current_page = paginator.get_page(pub_date)
    print(current_page)

    prev_page, next_page = None, None
    if current_page.has_previous():
        prev_page = current_page.previous_page_number()
        prev_page = '%s/' % prev_page
        print(prev_page)
    if current_page.has_next():
        next_page = current_page.next_page_number()
        next_page = '%s/' % next_page
        print(next_page)

    context = {'books': books}
    return render(request, template, context)