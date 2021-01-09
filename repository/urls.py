from django.urls import path

from . import views

app_name = 'repository'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('new-img-resource', views.RecursoImagenCreateView.as_view(), name='new-img-resource'),
]
