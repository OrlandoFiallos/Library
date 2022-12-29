from django.shortcuts import render
from .models import Libro,InstanciaLibro,Autor,Genero
from django.views import generic
# Create your views here.

def index(request):
    #Genera el conteo de todos los libros
    num_books = Libro.objects.all().count()
    num_instances = InstanciaLibro.objects.all().count()
    num_genres = Genero.objects.all().count()
    
    #Número de visitas a esta vista, contadas en la variable de sesión
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    
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
        'num_visits': num_visits
        
    }
    
    return render(request,'index.html',context=context)

#Vistas basadas en clase
class BookListView(generic.ListView):
    model = Libro
    #cambiar el nombre del contexto
    context_object_name = 'my_book_list'
    #cambiando el queryset
    # queryset = Libro.objects.filter(title__icontains='war')[:5]
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    #Agregando paginación
    paginate_by = 10
    #Sobreescribiendo algunos métodos
    # def get_queryset(self):
    #     return Libro.objects.filter(title__icontains='war')[:5]
    #Ordenando el queryset alfabéticamente por su atributo title
    def get_queryset(self):
        return Libro.objects.all().order_by('title')
    
    #Pasar variables adicionales sobreescribiendo el método get_context_data(self)
    
    def get_context_data(self, **kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context['new_data'] = 'Some new data'
        return context 
    
#Vistas basadas en clase vista de detalle
class BookDetailView(generic.DetailView):
    model = Libro 

class AuthorListView(generic.ListView):
    model = Autor 

class AuthorDetailView(generic.DetailView):
    model = Autor