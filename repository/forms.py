from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        
        # Agrega un atributo class con el mismo valor
        # a todos los campos del formulario.
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form__text'
            
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
         
