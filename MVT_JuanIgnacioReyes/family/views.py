from django.shortcuts import render
from django.http import HttpResponse
from family.models import Family
# Create your views here.

#? funcion para crear un miembro de la familia
def create_family_member(request):
    new_member = Family.objects.create(name = "prueba", surname = "html", age = 24 , dni = 5 , alive = True ) #ingresar los datos del miembro
    #imprimir el nuevo miembro creado en httpresponse
    return HttpResponse(f"usted creo un familiar: nombre: {new_member.name} - apellido: {new_member.surname} - edad: {new_member.age} - DNI: {new_member.dni} - vive?: {new_member.alive}")

#? funcion para crear listar todos los miembros de la familia
def list_family_members(request):
    all_family_members = Family.objects.all()
    context = {
        "family": all_family_members,
    }
    return render(request, "list_families.html", context=context)