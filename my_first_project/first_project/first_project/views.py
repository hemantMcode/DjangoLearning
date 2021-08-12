# this will store the functions which will direct the pages
# called from the url.py
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    user_input = request.GET['user_input']
    user_input = user_input.upper()
    user_input += "this is a text"
    return render(request, "about.html", {'home_input': user_input})

def result(request):
    return render(request, "result.html")
