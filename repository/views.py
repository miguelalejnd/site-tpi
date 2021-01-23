from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, views 
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .forms import (
    UserRegistrationForm, CustomAuthenticationForm,
    RecursoImagenCreateForm, RecursoSonidoCreateForm,
    RecursoLinkCreateForm
)
from .models import Recurso, RecursoImagen, RecursoSonido, RecursoEnlazado, Lista

# Create your views here.


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Recurso
    template_name = 'repository/index.html'
    context_object_name = 'recurso_lists'
    paginate_by = 10
    login_url = '/login/'


class FavoritesListView(LoginRequiredMixin, generic.ListView):
    model = Recurso
    template_name = 'repository/favorites.html'
    context_object_name = 'recurso_lists'
    paginate_by = 10
    login_url = '/login/'
    
    def get_queryset(self):
        return Recurso.objects.filter(lista__propietario=self.request.user, lista__tipo_lista = Lista.TIPO_FAVORITOS)


class SeeAfterListView(LoginRequiredMixin, generic.ListView):
    model = Recurso
    template_name = 'repository/see_after.html'
    context_object_name = 'recurso_lists'
    paginate_by = 10
    login_url = '/login/'

    def get_queryset(self):
        return Recurso.objects.filter(lista__propietario=self.request.user, lista__tipo_lista = Lista.TIPO_VER_MAS_TARDE)


class MyResourcesView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Recurso
    template_name = 'repository/myresources.html'
    context_object_name = 'recurso_lists'
    paginate_by = 10

    def get_queryset(self):
        return Recurso.objects.filter(propietario=self.request.user)

class SuperView(generic.detail.DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        '''
        new_context_entry_1 = self.object.list_set.filter(
            propietario=self.request.user,
            tipo_lista=Lista.TIPO_FAVORITOS
        ).exist()
        
        new_context_entry_2 = self.object.list_set.filter(
            propietario=self.request.user,
            tipo_lista=Lista.TIPO_VER_MAS_TARDE
        ).exist()
        
        context["is_fav"] = new_context_entry_1
        context["is_vms"] = new_context_entry_2
        '''
        try:
            if self.object.lista_set.get(propietario=self.request.user, tipo_lista=Lista.TIPO_FAVORITOS):
                new_context_entry_1 = True
        except ObjectDoesNotExist:
            new_context_entry_1 = False
        
        try:
            if self.object.lista_set.get(propietario=self.request.user, tipo_lista=Lista.TIPO_VER_MAS_TARDE):
                new_context_entry_2 = True
        except ObjectDoesNotExist:
            new_context_entry_2 = False
        
        context["is_fav"] = new_context_entry_1
        context["is_vms"] = new_context_entry_2
        
        return context


class RecursoImagenDetailView(SuperView):
    model = RecursoImagen

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)      
#        try:                
#            new_context_entry = True if self.object.get()
#        except RecursoImagen.DoesNotExist :
#            new_context_entry 
#    context["is_list_item"] = new_context_entry
#    return context


def async_fav(request, pk):
    if request.user.is_authenticated:
        recurso = get_object_or_404(Recurso, pk=pk)
        
        try:
            list = recurso.lista_set.get(propietario=request.user, tipo_lista=Lista.TIPO_FAVORITOS)
            list.delete()
            value = 'Agregar Favoritos'
        except Lista.DoesNotExist:
            new_list = Lista(tipo_lista=Lista.TIPO_FAVORITOS, propietario=request.user)
            new_list.save()
            recurso.lista_set.add(new_list)
            value = 'Eliminar de Favoritos'

        response = HttpResponse(value)
        response['Access-Control-Allow-Origin'] = '*'
        
        return response

def async_vms(request, pk):
    if request.user.is_authenticated:
        recurso = get_object_or_404(Recurso, pk=pk)
    
    try:
        list = recurso.lista_set.get(propietario=request.user, tipo_lista=Lista.TIPO_VER_MAS_TARDE )
        list.delete()
        value = 'Agregar a Ver más tarde'
    except Lista.DoesNotExist:
        new_list = Lista(tipo_lista=Lista.TIPO_VER_MAS_TARDE , propietario=request.user)
        new_list.save()
        recurso.lista_set.add(new_list)
        value = 'Eliminar de Ver más tarde'

    response = HttpResponse(value)
    response['Access-Control-Allow-Origin'] = '*'
    
    return response
    
    
class RecursoSonidoDetailView(SuperView):
    model = RecursoSonido


class RecursoEnlazadoDetailView(SuperView):
    model = RecursoEnlazado


class CustomLoginView(views.LoginView):
    authentication_form=CustomAuthenticationForm    


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
    
    def dispatch(self, request, *args, **kwargs):
        if self.object.propietario != self.request:
            raise Http404('No tiene permiso para editar este elemento.')
        return super(RecursoImagenUpdateView, self).dispatch(request, *args, **kwargs)


class RecursoImagenDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RecursoImagen
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_confirm_delete.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.object.propietario != self.request.user:
            raise Http404('No tiene permiso para eliminar este elemento.')
        return super(RecursoImagenDeleteView, self).dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        if self.object.propietario != self.request.user:
            raise Http404('No tiene permiso para editar este elemento.')
        return super(RecursoSonidoUpdateView, self).dispatch(request, *args, **kwargs)

class RecursoSonidoDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RecursoSonido
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        if self.object.propietario != self.request.user:
            raise Http404('No tiene permiso para eliminar este elemento.')
        return super(RecursoSonidoDeleteView, self).dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        if self.object.propietario != self.request.user:
            raise Http404('No tiene permiso para editar este elemento.')
        return super(RecursoLinkUpdateView, self).dispatch(request, *args, **kwargs)

class RecursoLinkDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RecursoEnlazado
    success_url = '/'
    login_url = '/login/'
    template_name = 'repository/recurso_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        if self.object.propietario != self.request.user:
            raise Http404('No tiene permiso para eliminar este elemento.')
        return super(RecursoLinkDeleteView, self).dispatch(request, *args, **kwargs)
    
