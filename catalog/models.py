from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genero(models.Model):
    name = models.CharField(max_length=200,help_text='Ingrese el nombre del género')

    def __str__(self):
        return self.name

class Libro(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Autor',on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length=1000,help_text='Ingrese una breve descripción del libro')
    isbn = models.CharField('ISBN',max_length=13,help_text='13 caracteres')
    genre = models.ManyToManyField(Genero,help_text='Seleccione un género para este libro')
    language = models.ForeignKey('Idioma',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])
    
    def display_genre(self):
        return ','.join([genre.name for genre in self.genre.all()[:3]])
    
    display_genre.short_description = 'Genre'

class InstanciaLibro(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4,help_text='ID único para este libro en toda la biblioteca')
    book = models.ForeignKey(Libro,on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True,help_text='Fecha de devolución')

    LOAN_STATUS = (
        ('M','Mantenimiento'),
        ('o','En préstamo'),
        ('a','Disponible'),
        ('r','Reservado'),
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='Disponibilidad del libro')

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return '%s (%s)' % (self.id,self.book.title)

class Autor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.last_name,self.first_name)
    
    class Meta:
        ordering = ['first_name']

class Idioma(models.Model):
    name = models.CharField('Idioma',max_length=20)

    def __str__(self):
        return self.name