from django.forms import ModelForm
from booklist.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
