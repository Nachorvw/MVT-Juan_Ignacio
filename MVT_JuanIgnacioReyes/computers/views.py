from django.shortcuts import render
from django.http import HttpResponse
from computers.models import Computer
# Create your views here.

def create_pc(request):
    new_pc = Computer.objects.create(serial_num = 2333142132, usage = False)
    return HttpResponse("se creo la pc")

def list_pc(request):
    all_pc = Computer.objects.all()
    context = {
        "computers": all_pc,
    }
    return render(request, "list_computers.html", context=context)