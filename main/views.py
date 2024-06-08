from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.items import flanes
from main.forms import ContactForm

# Create your views here.
def index(req):
  context = {'flanes': flanes}
  return render(req, 'index.html', context)

def about(req):
  return render(req, 'about.html')

def welcome(req):
    if req.method == 'GET':
        form = ContactForm() # Se crea una instancia del formulario FlanForm sin datos iniciales.
        context = {'form': form} # Se crea un contexto que contiene el formulario vacío.
        return render(req, 'welcome.html', context) # Se renderiza la plantilla 'welcome.html' con el contexto.
    else:
        form = ContactForm(req.POST) # Se crea una instancia de FlanForm con los datos enviados en la solicitud POST.
        if form.is_valid(): # Se verifica si los datos del formulario son válidos.
            return redirect('/success') # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form} # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(req, 'welcome.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.

def success(req):
  return render(req, 'success.html')

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
    return render(req, )
  # ahora tengo que validar que customer name tenga al menos un @ y un . 
  # by que customr_name sea de largo maximo 64 (lenght)
  # si len(errores) == 0: redirijo a página de éxito
  # si len(errores) > 0: vuelvo a cargar 'welcome.html', pero ahora mostrando los errores
  
  '''