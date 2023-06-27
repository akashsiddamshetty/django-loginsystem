from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('hello world')


def signup(request):
    return HttpResponse('singup page')


def login(request):
    return HttpResponse('login poage')

def logout(request):
    return HttpResponse('logout ')