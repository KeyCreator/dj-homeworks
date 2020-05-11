from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from books.models import Book

def index(request):
    return redirect(reverse(books_view))

def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {}
    if pub_date:
        print(f'pub_date={pub_date}, {type(pub_date)}')

        ' Делаем собственный пагинатор '
        pub_dates = map(lambda book: book.pub_date, books)   # Получаем перечень дат выхода книг
        pub_dates = set(pub_dates)  # отсекаем все дублирующиеся записи
        prev_page, next_page = None, None
        for item in sorted(pub_dates):
            if pub_date < item:
                next_page = item
                context.setdefault('next_page', f'{reverse(books_view)}/{next_page}/')
                break
        for item in sorted(pub_dates, reverse=True):
            if pub_date > item:
                prev_page = item
                context.setdefault('prev_page', f'{reverse(books_view)}/{prev_page}/')
                break

        print(f'prev_date={prev_page}, {type(prev_page)}')
        print(f'next_date={next_page}, {type(next_page)}')

        books = filter(lambda book: book.pub_date == pub_date, books)

    books = list(books)
    print(books, type(books))
    context.setdefault('books', books)
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