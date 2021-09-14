from django.shortcuts import render
from .models import Laptop
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class LaptopListView(ListView):
    model = Laptop

class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/lap/list/'

class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/lap/list/'

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = '/lap/list/'

def home(request):
    tempalte_name = 'LaptopApp/home.html'
    context = {}
    return render(request, tempalte_name, context)

