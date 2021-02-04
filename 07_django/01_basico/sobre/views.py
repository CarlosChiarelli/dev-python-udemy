from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Sobre: eu sou Carlos!')


def teste(request):
    return render(request, 'sobre/assunto.html')
