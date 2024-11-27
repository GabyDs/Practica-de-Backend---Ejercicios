from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("list_users/", views.list_users, name="list_users")
]
