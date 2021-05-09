from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return render(request,'home.html', {})

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    ordering = ['-date_added']
    # ordering = ['-id']
    # ordering was set like this to get most recentadded products  at top, just a hackk

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'

class UpdateProductView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    success_url = reverse_lazy('home')
    # form_class = ProductForm
    fields = '__all__'

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')
    

