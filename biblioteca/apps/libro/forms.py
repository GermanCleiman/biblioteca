from django import forms
from .models import Autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
        'nombre',
        'apellidos',
        'nacionalidad',
        'descripcion'
        ]
        labels = {
        'nombre': 'Nombre del autor',
        'apellidos': 'Apellidos del autor',
        'nacionalidad': 'Nacionalidad del autor',
        'descripcion': 'Reseña'
        }
        # paramas detalles de los widgets, docs.djangoproject.com 'widgets'
        widgets = {
                'nombre': forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder': 'Ingrese el Nombre del autor',
                        'id': 'nombre'
                            }
                        ),
                'apellidos': forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder': 'Ingrese los Apellidos del autor',
                        'id': 'apellidos'
                            }
                        ),
                'nacionalidad': forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder': 'Ingrese la Nacionalidad del autor',
                        'id': 'nacionalidad'
                            }
                        ),
                'descripcion': forms.Textarea(
                    attrs = {
                        'class': 'form-control',
                        'placeholder': 'Ingrese la Reseña del autor',
                        'id': 'descripcion'
                            }
                        ),
                    }
