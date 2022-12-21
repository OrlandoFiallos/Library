from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Autor)
# admin.site.register(Libro)
# admin.site.register(InstanciaLibro)
admin.site.register(Idioma)
admin.site.register(Genero)

#Configuración avanzada del sitio de administración 
# Vistas de lista:
# Añadir campos e información adicional desplegada para cada registro.
# Añadir filtros para seleccionar qué registros se listan, basados en fechas u otros tipos de valores (ej. estado de préstamo del libro).
# Añadir opciones adicionales al menú Action en las vistas de lista y elegir en qué lugar del formulario se despliega este menú.
# Vistas de detalle:
# Elegir qué campos desplegar (o excluir), junto con su orden, agrupamiento, si son editables, el tipo de control a usarse, orientación, etc.
# Añadir campos relacionados a un registro para permitir la edición en cadena (ej. proveer la capacidad de añadir y editar registros de libros mientras estás creando su registro de autor).

#clase para edición en cadena de registros asociados
#admin.TabularInline para mostrar los registros de manera horizontal
class InstanciaLibroInline(admin.TabularInline):
    model = InstanciaLibro
    #por defecto nos muestra 3 instancias vacías, con el atributo extra podemos controlar la cantidad de instancias que queremos mostrar
    extra = 0

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    
    #edición en cadena de registros asociados
    inlines = [InstanciaLibroInline]
    
class LibroInline(admin.TabularInline):
    model = Libro
    extra = 0

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth')
    #ordenando la vista detallada, si los campos se agrupan en tuplas se despliegan uno al lado del otro (por defecto se despliegan en vertical)
    fields = [('first_name','last_name'),'date_of_birth']
    #Exclude para excluir un campo que no queramos mostrar
    # exclude = ['date_of_birth']
    
    inlines = [LibroInline]

@admin.register(InstanciaLibro)
class InstanciaLibroAdmin(admin.ModelAdmin):
    #campos a mostrar
    list_display = ('id','book','status','due_back')
    #añadiendo filtro
    list_filter = ('status','due_back')
    
    #seccionando la vista de detalle
    fieldsets = (
        ('Book data',{
            'fields':('book','imprint','id')
        }),
        ('Availavility',{
            'fields':('status','due_back')
        })
    )