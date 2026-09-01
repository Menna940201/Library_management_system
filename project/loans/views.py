from catalog.models import Book 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Loan


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    existing_loan = Loan.objects.filter(
        member=request.user, book=book, status="borrowed"
    ).exists()

    if existing_loan:
        messages.error(request, "You already borrowed this book.")
        return redirect("book_list")

    if book.available_copies <= 0:
        messages.error(request, "No available copies of this book.")
        return redirect("book_list")

    Loan.objects.create(member=request.user, book=book)
    book.available_copies -= 1
    book.save()
    messages.success(request, f"You borrowed '{book.title}' successfully.")
    return redirect("book_list")


# @login_required
def my_loans(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in first.")
        return redirect("login")
    loans = Loan.objects.filter(member=request.user, status="borrowed").order_by("-borrow_date")
    return render(request, "loans/loan.html", {"loans": loans})


@login_required
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, member=request.user, status="borrowed")
    loan.status = "returned"
    loan.return_date = timezone.now()
    loan.save()
    loan.book.available_copies += 1
    loan.book.save()
    messages.success(request, f"You returned '{loan.book.title}' successfully.")
    return redirect("my_loans")
