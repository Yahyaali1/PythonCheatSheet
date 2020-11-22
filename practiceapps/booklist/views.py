from booklist.forms import BookForm
from booklist.models import Book
from booklist.utils import get_alert_message
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_http_methods
from rest_framework import generics, mixins
from rest_framework import serializers


class BookView(LoginRequiredMixin, View):
    login_url = reverse_lazy("booklist:login")

    def get(self, request):
        add_book_form = None
        alert_messages = []
        alert_message = request.session.get("alert", None)
        if alert_message:
            alert_messages.append(alert_message)
            del request.session['alert']
        if not request.user.is_staff:
            user_book_list = request.user.books.all()
            add_book_form = BookForm(initial={'owner': request.user.id})
        else:
            user_book_list = Book.objects.all()

        return render(request, template_name="booklist/booklisting.html", context={'form': add_book_form,
                                                                                   'books': user_book_list,
                                                                                   'alerts': alert_messages})

    def post(self, request):
        alert_messages = []
        book_form = BookForm(request.POST)
        user_book_list = Book.objects.all()if request.user.is_staff else request.user.books.all()

        if book_form.is_valid():
            book_form.save(user=request.user)
            alert_messages.append(get_alert_message("Book Added", error=False))
            book_form = BookForm(initial={'owner': request.user.id})

        print(book_form)
        return render(request, template_name="booklist/booklisting.html", context={'form': book_form,
                                                                                   'books': user_book_list,
                                                                                   'alerts': alert_messages})


@login_required(login_url=reverse_lazy("booklist:login"))
@permission_required('user.is_staff', raise_exception=True)
@require_http_methods(["POST"])
def delete_book_view(request):
    book = get_object_or_404(Book, pk=request.POST['book_id'])
    book.delete()
    request.session['alert'] = get_alert_message("Book Deleted", error=False)
    return redirect('booklist:home')


def logout_view(request):
    logout(request)
    return redirect('booklist:login')

