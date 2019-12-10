from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from booklist.forms import BookForm
from booklist.models import Book


class BookView(LoginRequiredMixin, View):
    login_url = reverse_lazy("booklist:login")

    def get(self, request):
        add_book_form = None if request.user.is_staff else BookForm(initial={'owner': request.user.id})
        user_book_list = Book.objects.all() if request.user.is_staff else Book.objects.filter(owner__id=request.user.id)

        return render(request, template_name="booklist/booklisting.html", context={'form': add_book_form,
                                                                                   'books': user_book_list})

    def post(self, request):
        book_form = BookForm(request.POST)
        print(request.POST)
        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect(reverse_lazy("booklist:home"))
        return HttpResponse('Error')
