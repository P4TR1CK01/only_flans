from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.items import flanes
from main.forms import ContactForm
from main.models import Contact

# Create your views here.
def index(req):
  context = {'flanes': flanes}
  return render(req, 'index.html', context)

def welcome(req):
  #esto debe mostrar solo los flanes privados de la base de datos
  return render(req, 'welcome.html')

def about(req):
  return render(req, 'about.html')

def ayuda(req):
  return render(req, 'help.html')

def contact(req):
    if req.method == 'GET':
        form = ContactForm()                            # Se crea una instancia del formulario FlanForm sin datos iniciales.
        context = {'form': form}                        # Se crea un contexto que contiene el formulario vacío.
        return render(req, 'contact.html', context)     # Se renderiza la plantilla 'welcome.html' con el contexto.
    else:
        form = ContactForm(req.POST)                    # Se crea una instancia de FlanForm con los datos enviados en la solicitud POST.
        if form.is_valid():                             # Se verifica si los datos del formulario son válidos.
            Contact.objects.create(
              **form.cleaned_data
            )
            return redirect('/success')                 # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form}                        # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(req, 'contact.html', context)     # Se vuelve a renderizar la plantilla con el contexto actualizado.

def success(req):
  return render(req, 'success.html')

def login(req):
  return render(req, 'login.html')

def register(req):
  return render(req, 'register.html')




  # ahora tengo que validar que customer name tenga al menos un @ y un . 
  # by que customr_name sea de largo maximo 64 (lenght)
  # si len(errores) == 0: redirijo a página de éxito
  # si len(errores) > 0: vuelvo a cargar 'welcome.html', pero ahora mostrando los errores  
'''
errores = [] 
  if len(customer_name) > 5:
    errores.append('Excede el número permitido  de caracteres, utilíce un máximo de 65 caracteres')
  
  if not '@' in customer_email:
    errores.append('Utilice un e-mail válido que contenga al menos un @')
  context = {'error': errores}
  
  if len(errores) > 0:
    return render(req, 'welcome.html',context)
  
  else:
    return render(req, errores)
'''