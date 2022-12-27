from django.shortcuts import render
from django.http import HttpResponse
from family.models import Family
# Create your views here.

#? funcion para crear un miembro de la familia
def create_family_member(request):
    #usando variables para una mejor lectura y edicion de los valores
    name = "Juan Ignacio"
    surname = "Reyes"
    age = 24
    dni = 12123333
    alive = True
    new_member = Family.objects.create(name = name, surname = surname, age = age , dni = dni, alive = alive ) #ingresar los datos del miembro
    context = { 
        "new_member" : new_member
    }
    return render(request, "creacion_family.html", context=context)

#? funcion para crear listar todos los miembros de la familia
def list_family_members(request):
    all_family_members = Family.objects.all()
    context = {
        "family": all_family_members,
    }
    return render(request, "list_families.html", context=context)