from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from booklist.forms import BookForm


class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("booklist:login")

    def get(self, request):
        add_book_form = BookForm(initial={'owner': request.user.id+1})
        return render(request, template_name="booklist/booklisting.html", context={'form': add_book_form})


class BookView(LoginRequiredMixin, View):
    login_url = reverse_lazy("booklist:login")

    def post(self, request):
        print(request.POST)
        return HttpResponse('Welcome')
