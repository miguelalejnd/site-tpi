from django.urls import path

from . import views

app_name = 'repository'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('new-img-resource', views.RecursoImagenCreateView.as_view(), name='new-img-resource'),
    path('<int:pk>/edit-img-resource', views.RecursoImagenUpdateView.as_view(), name='edit-img-resource'),
    path('<int:pk>/delete-img-resource', views.RecursoImagenDeleteView.as_view(), name='delete-img-resource'),
    path('new-audio-resource', views.RecursoSonidoCreateView.as_view(), name='new-audio-resource'),
    path('<int:pk>/edit-audio-resource', views.RecursoSonidoUpdateView.as_view(), name='edit-audio-resource'),
    path('<int:pk>/delete-audio-resource', views.RecursoSonidoDeleteView.as_view(), name='delete-audio-resource'),
    path('new-link-resource', views.RecursoLinkCreateView.as_view(), name='new-link-resource'),
    path('<int:pk>/edit-link-resource', views.RecursoLinkUpdateView.as_view(), name='edit-link-resource'),
    path('<int:pk>/delete-link-resource', views.RecursoLinkDeleteView.as_view(), name='delete-link-resource'),
]

