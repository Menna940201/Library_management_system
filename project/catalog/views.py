from django.shortcuts import render
from .models import Book
from django.db.models import Sum

def book_list(request):
    books = Book.objects.all()
    total_copies = Book.objects.aggregate(
        total=Sum("total_copies")
    )["total"] or 0
    available_copies = Book.objects.aggregate(
        total=Sum("available_copies")
    )["total"] or 0
    borrowed_copies = total_copies - available_copies
    return render(request, 'catalog/book_list.html', {
        'books': books,
        'total_copies': total_copies,
        'available_copies': available_copies,
        'borrowed_copies': borrowed_copies
    })

def about_us(request):
    return render(request, 'about.html')