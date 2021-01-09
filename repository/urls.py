from django.urls import path

from . import views

app_name = 'repository'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('new', views.new_resource, name='new_resource'),
]
