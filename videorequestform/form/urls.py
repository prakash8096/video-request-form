
from django.urls import path
from . import views

urlpatterns = [

   path('',views.Vdata,name='home'),
   path('forms/',views.Vrform,name='forms'),
]