from django.shortcuts import render
from django.http import HttpRequest


def show_home_page(request: HttpRequest):
    return render(request, "main/index.html")
