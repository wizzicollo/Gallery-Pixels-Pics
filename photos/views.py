from django.shortcuts import render

# Create your views here.

def home(request):
    images = Picture.objects.all()
    return render (request, 'home.html', {"images":images})