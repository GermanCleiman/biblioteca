from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor
from django.views.generic import TemplateView, ListView

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# cuando ingrese una url (request'pedido desde el navegador) hace...
# render , pintar en..parametros(request, template a pintar)
# -------------paso de funciones a clases--------------------
#def home(request):
#    return render(request, 'index.html')

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


class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)


def editarAutor(request,id):
    autor_form = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')
    except ObjectDoesNotExist as e:
        error = e
    error = None
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error':error})

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
