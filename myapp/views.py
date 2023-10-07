from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest,HttpResponse
# Create your views here.
def myfunc(request):
    return HttpResponse('<h1>Login</h1>')

def myfunc2(request):
    return HttpResponse('<h1>Home</h1>')