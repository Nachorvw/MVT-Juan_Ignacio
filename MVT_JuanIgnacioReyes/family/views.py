from django.shortcuts import render
from django.http import HttpResponse
from family.models import Family
# Create your views here.

def create_family_member(request):
    new_member = Family.objects.create(name = "rodrigo", surname = "trillo", age = 22 , dni= 123455123 , alive = True ) #datetime = año, dia, mes
    return HttpResponse("se creo el familiar")

def list_family_members(request):
    all_family_members = Family.objects.all()
    context = {
        "family": all_family_members,
    }
    return render(request, "list_families.html", context=context)