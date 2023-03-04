# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Você está na home")


def contact(request):
    return HttpResponse("Você está na página de contato")


def about(request):
    return HttpResponse("Você está na página Sobre")
