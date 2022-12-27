from django.shortcuts import render
from products.models import Products

# Create your views here.
#?funcion para crear productos
def create_products(request):
    #usando variables para una mejor lectura y edicion de los valores
    name = "Coca Cola"
    cuantity = 10
    price = 150
    available = True
    description = "Coca Cola 500ml"
    new_product = Products.objects.create(name = name, cuantity = cuantity, price = price, available = available, description = description)
    context = {
        "new_product" : new_product 
    }
    return render(request, "create_product.html", context=context)

#?funcion para listar productos
def list_products(request):
    all_products = Products.objects.all()
    context = {
        "Products": all_products,
    }
    return render(request, "list_products.html", context={})