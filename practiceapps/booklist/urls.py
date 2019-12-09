from django.urls import path
from booklist.views import HomeView, BookView
from django.contrib.auth.views import LoginView

app_name = "booklist"
urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("login", LoginView.as_view(template_name="booklist/login.html"), name='login'),
    path("add_book", BookView.as_view(), name='add_book'),
]
