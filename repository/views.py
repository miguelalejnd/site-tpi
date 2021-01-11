from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, views 
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    UserRegistrationForm, CustomAuthenticationForm,
    RecursoImagenCreateForm, RecursoSonidoCreateForm,
    RecursoLinkCreateForm
)
from .models import Recurso, RecursoImagen, RecursoSonido, RecursoEnlazado

# Create your views here.


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Recurso
    template_name = 'repository/index.html'
    context_object_name = 'recurso_lists'
    paginate_by = 10
    login_url = '/login/'

class MyResourcesView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Recurso
    template_name = 'repository/myresources.html'
    context_object_name = 'recurso_lists'
    paginate_by = 10

    def get_queryset(self):
        return Recurso.objects.filter(propietario=self.request.user)

class RecursoImagenDetailView(generic.detail.DetailView):
    model = RecursoImagen


class RecursoSonidoDetailView(generic.detail.DetailView):
    model = RecursoSonido


class RecursoEnlazadoDetailView(generic.detail.DetailView):
    model = RecursoEnlazado

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
    template_name = 'repository/recurso_form.html'
    
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        
        return super().form_valid(form)

class RecursoImagenUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = RecursoImagen
    form_class = RecursoImagenCreateForm
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_form.html'
    
    #def get_context_data(self, **kwargs):
   #      context = super().get_context_data(**kwargs)
     #    context['update'] = True
        
      #   return context


class RecursoImagenDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RecursoImagen
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_confirm_delete.html'

class RecursoSonidoCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = RecursoSonido
    form_class = RecursoSonidoCreateForm
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_form.html'
    
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        
        return super().form_valid(form)


class RecursoSonidoUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = RecursoSonido
    form_class = RecursoSonidoCreateForm
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_form.html'


class RecursoSonidoDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RecursoSonido
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_confirm_delete.html'


class RecursoLinkCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = RecursoEnlazado
    form_class = RecursoLinkCreateForm
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_form.html'
    
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        
        return super().form_valid(form)

class RecursoLinkUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = RecursoEnlazado
    form_class = RecursoLinkCreateForm
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_form.html'


class RecursoLinkDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RecursoEnlazado
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_confirm_delete.html'
