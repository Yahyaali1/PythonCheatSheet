from django.forms import ModelForm
from booklist.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ["owner", ]

    def save(self, user, commit=True,):

        self.instance.owner = user
        return super().save(commit)
