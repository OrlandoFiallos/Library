# Generated by Django 3.2.16 on 2022-12-15 21:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre del género', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Ingrese una breve descripción del libro', max_length=1000)),
                ('isbn', models.CharField(help_text='13 caracteres', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.autor')),
                ('genre', models.ManyToManyField(help_text='Seleccione un género para este libro', to='catalog.Genero')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.idioma')),
            ],
        ),
        migrations.CreateModel(
            name='InstanciaLibro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para este libro en toda la biblioteca', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('M', 'Mantenimiento'), ('o', 'En préstamo'), ('a', 'Disponible'), ('r', 'Reservado')], default='m', help_text='Disponibilidad del libro', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.libro')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
