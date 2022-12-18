from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()
    return render(request,'shop/index.html',{'products':products})

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/shop/')
    else:
        form = ProductForm()
    
    return render(request, 'shop/create.html', {'form': form})

def edit(request, slug):
    product = Product.objects.get(id=slug)
    form = ProductForm(request.POST or None, instance = product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/shop/')
    
    return render(request, 'shop/edit.html', {'form': form, 'id': slug})

def delete(request,slug):
    toDelete = Product.objects.get(id=slug)
    toDelete.delete()
    return HttpResponseRedirect('/shop/')

def show(request,slug):
    product = Product.objects.get(id=slug)
    return render(request,'shop/show.html',{'product':product})
