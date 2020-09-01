from django.shortcuts import render, redirect
from . forms import PersonaForms
from django.core.exceptions import ObjectDoesNotExist
from . models import Persona

def Home(request):
    return render(request, 'Home.html')

def crearPersona(request):
    if request.method == 'POST':
    
        nom = request.POST.get("nombre")
        ape = request.POST.get("apellido")
        naci = request.POST.get("nacionalidad")
        desc = request.POST.get("descripcion")
        per = Persona(nombre = nom, apellido = ape, nacionalidad = naci, descripcion = desc)
        per.save()
        return render(request, 'Home.html')
    else:
            perForm = PersonaForms()
            print(perForm)
    return render(request, 'Persona/crearPersona.html',{'perForm':perForm})


def editarPersona(request, id):
    perform = None
    error = None
    try:
        per = Persona.objects.get(id = id)
        if request.method == 'GET' :
           perform = PersonaForms(instance = per)
        else:
            perform = PersonaForms(request.POST, instance = per)
            if perform.is_valid():
                perform.save()
            return render(request, 'Home.html')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'persona/editarPersona.html',{'perform':perform, 'error': error, 'persona':per})  
    
def listarPersona(request):
    personas = Persona.objects.filter(estado = True)
    return render(request, 'Persona/listarPersona.html', {'personas':personas})

    
def eliminarPersona(request, id):
    personas = Persona.objects.get(id = id)
    personas.estado = False
    personas.save()
    return redirect('persona:listarPersona')