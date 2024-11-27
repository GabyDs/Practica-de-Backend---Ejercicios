from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.urls import reverse

from .models import User

def login_view(request):
    # Renderizar el template
    return render(request, "login.html")

def list_users(request):

    users = User.objects

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username, password=password).exists():
            return render(request, "list_users.html", {'users': users})
        else:
            return HttpResponseRedirect(reverse("users:login_view"))