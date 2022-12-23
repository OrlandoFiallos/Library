from django.shortcuts import render
from .models import Libro,InstanciaLibro,Autor,Genero
# Create your views here.

def index(request):
    #Genera el conteo de todos los libros
    num_books = Libro.objects.all().count()
    num_instances = InstanciaLibro.objects.all().count()
    num_genres = Genero.objects.all().count()
    
    #Número de instancias disponibles filtradas por a (available)
    num_instances_available = InstanciaLibro.objects.filter(status__exact='a').count()
    num_authors = Autor.objects.all().count()
    num_books_with_de_word = Libro.objects.filter(title__icontains='de').count()
    
    #Definiendo el contexto
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_genres':num_genres,
        'num_books_with_de_word':num_books_with_de_word,
        
    }
    
    return render(request,'index.html',context=context)