from django.http import HttpRequest
from django.shortcuts import render


def base(request: HttpRequest):
    return render(request, 'base.html')


def home(request: HttpRequest):
    return render(request, 'home.html')
