from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Sum
from .forms import BookForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


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

@staff_member_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'catalog/add_book.html', {'form': form})

@staff_member_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'catalog/edit_book.html', {'form': form, 'book': book})

@staff_member_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect('book_list')