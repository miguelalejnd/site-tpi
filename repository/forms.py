from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import RecursoImagen, RecursoSonido, RecursoEnlazado

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        
        # Agrega un atributo class con el mismo valor
        # a todos los campos del formulario.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form__text'
        
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Contraseña (confirmación)'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Un nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Un apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'Dirección de correo electrónico'
            
    first_name = forms.CharField(
        max_length=150,
        required=False
    )
    last_name = forms.CharField(
        max_length=150,
        required=False
    )
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        
        # Agrega un atributo class con el mismo valor
        # a todos los campos del formulario.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form__text'
        
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
         

class RecursoImagenCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecursoImagenCreateForm, self).__init__(*args, **kwargs)
        
        # Agrega un atributo class con el mismo valor
        # a todos los campos del formulario.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['descripcion'].widget.attrs['placeholder'] = 'Descripción'

    class Meta:
        model = RecursoImagen
        fields = ['nombre', 'descripcion', 'categoria', 'archivo']

class RecursoSonidoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecursoSonidoCreateForm, self).__init__(*args, **kwargs)
        
        # Agrega un atributo class con el mismo valor
        # a todos los campos del formulario.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['descripcion'].widget.attrs['placeholder'] = 'Descripción'

    class Meta:
        model = RecursoSonido
        fields = ['nombre', 'descripcion', 'categoria', 'archivo']


class RecursoLinkCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecursoLinkCreateForm, self).__init__(*args, **kwargs)
        
        # Agrega un atributo class con el mismo valor
        # a todos los campos del formulario.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['descripcion'].widget.attrs['placeholder'] = 'Descripción'
        self.fields['url'].widget.attrs['placeholder'] = 'URL'

    class Meta:
        model = RecursoEnlazado
        fields = ['nombre', 'descripcion', 'categoria', 'url']
