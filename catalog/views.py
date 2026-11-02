from django.shortcuts import render,get_object_or_404

from .models import Product

def product_list(request):
    products = Product.objects.all()
    # կամ products = Product.objects.select_related('category').all()
    return render(request, "catalog/index.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "catalog/furniture-details.html", {"product": product})
