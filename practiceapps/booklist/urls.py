from django.urls import path
from booklist.views import HomeView
from django.contrib.auth.views import LoginView

app_name = "booklist"
urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("login", LoginView.as_view(redirect_field_name='home'), name='login'),
]
