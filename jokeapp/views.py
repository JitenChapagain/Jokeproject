from django.shortcuts import render,HttpResponse
import pyjokes

# Create your views here.
def home(request):
    joke=pyjokes.get_joke()
    return render(request, "index.html", {"joke":joke})