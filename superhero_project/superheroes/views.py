from django.shortcuts import render
from django.http import HttpResponse

from .models import Superhero


# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    return render(request, 'superheroes/index.html')