from django.shortcuts import render
from galeria.models import fotografia



def index(request):
    fotografias = fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem (request):
    return render(request, 'galeria/imagem.html')