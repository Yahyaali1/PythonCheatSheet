from django.urls import path
from booklist.views import BookView
from django.contrib.auth.views import LoginView

app_name = "booklist"
urlpatterns = [
    path("", BookView.as_view(), name='home'),
    path("login", LoginView.as_view(template_name="booklist/login.html"), name='login'),
    path("addbook", BookView.as_view(), name='add_book'),
]
