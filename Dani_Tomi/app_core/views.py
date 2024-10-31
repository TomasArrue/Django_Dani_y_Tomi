from django.shortcuts import render,redirect
from django.views.generic import CreateView, FormView
from .models import Gasto
from .forms import FormularioGasto
# Create your views here.

class FormGastoView(CreateView):
    model = Gasto
    form_class= FormularioGasto
    template_name = 'formulario.html'
    # success_url = '/thanks/'

    def form_valid(self, form):
        print('exito')
        return redirect('app_core:formulario')
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)