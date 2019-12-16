from django.urls import path
from booklist.views import BookView, logout_view, delete_book_view
from django.contrib.auth.views import LoginView

app_name = "booklist"
urlpatterns = [
    path("home", BookView.as_view(), name='home'),
    path("login", LoginView.as_view(template_name="booklist/login.html"), name='login'),
    path("logout", logout_view, name='logout'),
    path("addbook", BookView.as_view(), name='add_book'),
    path("delbook", delete_book_view, name='del_book')
]
