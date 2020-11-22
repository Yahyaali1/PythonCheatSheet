from django.shortcuts import redirect


def index_page(request):
    return redirect('booklist:home')
