from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render (request, "index.html")

def courses(request):
    return render (request, "courses.html")

def about(request):
    return render (request, "about.html")

def result(request):
    return render (request, "result.html")



def notes_page(request):
    return render (request, "notes.html")

def contact(request):
    return render (request,"contact.html")
