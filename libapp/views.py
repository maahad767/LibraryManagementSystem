from django.core.paginator import Paginator

from django.shortcuts import render
from django.views import View

from .models import *
from .filters import *


class MainView(View):
    def get(self, request):
        
        # categories = Category.objects.all()
        context = {
            
        }
        return render(request, 'libapp/main.html', context=context)


class BooksListView(View):
    def get(self, request):
        books = Book.objects.all()
        
        book_filter = BookFilter(request.GET, queryset=books.order_by('id'))
        filtered_books = book_filter.qs

        paginator = Paginator(filtered_books, 20) 

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'books': filtered_books,
            'page_obj': page_obj,
        }
        return render(request, 'libapp/books.html', context=context)