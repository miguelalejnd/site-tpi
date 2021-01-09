from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, views 
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegistrationForm, CustomAuthenticationForm, RecursoImagenCreateForm
from .models import Recurso, RecursoImagen

# Create your views here.


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Recurso
    template_name = 'repository/index.html'
    context_object_name = 'recurso_lists'
    paginate_by = 10
    login_url = '/login/'
    
    def get_queryset(self):
        return Recurso.objects.filter(propietario=self.request.user)

class CustomLoginView(views.LoginView):
    authentication_form=CustomAuthenticationForm    

@login_required
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(generic.ListView)
        if form.is_valid():
            
           user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password2'],
                email = form.cleaned_data['email'])
        
           # Evaluar si hay parametros extra y guardar.
           extra_args = False
           if 'first_name' in form.cleaned_data:
               user.first_name = form.cleaned_data['first_name']
               extra_args = True
           if  'last_name' in form.cleaned_data:
               user.last_name = form.cleaned_data['last_name']
               extra_args = True
           extra_args and user.save()
        
           login(request, user)
            
           return redirect(to='/')
        else:
            return render(
                request,
                template_name='registration/registro.html',
                context={'form': form})
    else:
        form = UserRegistrationForm()
    
    return render(
        request,
        template_name='registration/registro.html',
        context={'form': form})
        
class RecursoImagenCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = RecursoImagen
    form_class = RecursoImagenCreateForm
    success_url = '/'
    login_url = '/login/'
    
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        
        return super().form_valid(form)
