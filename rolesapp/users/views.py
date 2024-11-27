from django.shortcuts import render

from django.http import HttpResponse

def login_view(request):
    # Renderizar el template
    return render(request, "login.html")

def list_users(request):
    return HttpResponse("Vista de lista de usuarios")