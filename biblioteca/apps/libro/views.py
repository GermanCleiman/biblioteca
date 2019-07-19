from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# cuando ingrese una url (request'pedido desde el navegador) hace...
# render , pintar en..parametros(request, template a pintar)
# ------------- clases--------------------

class Inicio(TemplateView):
    template_name = 'index.html'

'''
Que hace TemplateView dependiente de View ?

de view:

1. El metodo dispatch(): que esta dentro de View elige el metodo (post, get ,etc) de HTTP para la solicitud.
2. http_method_not_allowed(): retorna un error cuando se utiliza un metodo http no soportado o edfinido.
3. options(): da la lista de nombres permitidos para la vista

de TemplateView:

class TemplateView(view):

    model =''
    template_name = ''
    context_object_name = ''
    queryset = Model.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, template_name)

'''
'''
def crearAutor(request):
    if request.method == 'POST':
    #----------- formato django automatico-----------------
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():   # cuando uso el is_valid django guarda la info # -*- coding: utf-8 -*-
            # cleaned_data, la recupero , nom=autor_form.cleaned_data('nombre', etc) y print(nom)#
            autor_form.save()
            return redirect('libro:listar_autor')
    # ---------------------------------------------------
    #--------- formato comun html----------------------------
        #nom= request.POST.get('nombre')
        #ape= request.POST.get('apellidos')
        #nacio= request.POST.get('nacionalidad')
        #desc= request.POST.get('descripcion')
        #autor = Autor(nombre = nom, apellidos = ape, nacionalidad = nacio, descripcion = desc)
        #autor_form.save()
        #return redirect('index')
    else:
        autor_form = AutorForm()
        return render(request,'libro/crear_autor.html', {'autor_form':autor_form})
'''

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

class EliminarAutor(DeleteView):
    model = Autor
    # redefino el post de DeleteView para que no use el que viene por defecto
    def post(self, request, pk,*args, **kwargs):
        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')


'''
def eliminarAutor (request,id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        #autor.delete()     # eliminacion fisica
        # --------- eliminacion logica !!!
        autor.estado = False
        autor.save()
        # ---------------------------------
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html', {'autor': autor})
'''
