from django.shortcuts import render
from django.http import HttpResponse
from family.models import Family
# Create your views here.

#? funcion para crear un miembro de la familia
def create_family_member(request):
    new_member = Family.objects.create(name = "prueba", surname = "html", age = 24 , dni = 3 , alive = True ) #ingresar los datos del miembro
    new_member_data = Family.objects.latest('id')
    context = {
        "new_member_data" : new_member_data    #intente hacer que te muestre en creacion_family.html el miembro que se creo (no pude jeje)
    }
    return render(request, "creacion_family.html", context=context)

#? funcion para crear listar todos los miembros de la familia
def list_family_members(request):
    all_family_members = Family.objects.all()
    context = {
        "family": all_family_members,
    }
    return render(request, "list_families.html", context=context)