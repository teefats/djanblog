from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello there<h1>')
# def home(request):
#     return render('request', 'blog/home.html')

def about(request):
    return HttpResponse('<h2>About us</h2>')