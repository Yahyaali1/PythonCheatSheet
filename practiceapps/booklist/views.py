from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from booklist.forms import BookForm
from booklist.models import Book
from booklist.utils import get_alert_message


class BookView(LoginRequiredMixin, View):
    login_url = reverse_lazy("booklist:login")

    def get(self, request):
        add_book_form = None
        if not request.user.is_staff:
            user_book_list = Book.objects.filter(owner__id=request.user.id)
            add_book_form = BookForm(initial={'owner': request.user.id})
        else:
            user_book_list = Book.objects.all()

        return render(request, template_name="booklist/booklisting.html", context={'form': add_book_form,
                                                                                   'books': user_book_list})

    def post(self, request):
        alert_messages = []
        book_form = BookForm(request.POST)
        user_book_list = Book.objects.all() if request.user.is_staff else Book.objects.filter(owner__id=request.user.id)
        if book_form.is_valid():
            book_form.save()
            alert_messages.append(get_alert_message("Book Added", error=False))
            book_form = BookForm(initial={'owner': request.user.id})

        return render(request, template_name="booklist/booklisting.html", context={'form': book_form,
                                                                                   'books': user_book_list,
                                                                                   'alerts': alert_messages})
