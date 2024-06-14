from django import forms

class ContactForm(forms.Form):
  nombre = forms.CharField(   
    max_length=64,
    widget=forms.TextInput(attrs={
      'class': 'form-control mb-3',
      'placeholder': 'Escriba su nombre'
      })
)
  email = forms.EmailField(
    label='Correo Electronico',
    widget=forms.EmailInput(attrs={
      'class':'form-control mb-3',
      'placeholder': 'Ingrese su Correo Electronico'
      })
)
  mensaje = forms.CharField(
    max_length=64,
    widget=forms.Textarea(attrs={
      'class': 'form-control mb-3', 
      'rows': 5,
      'placeholder': 'Ingrese aquí su mensaje'
      })
)   
  
class RegisterForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField()
  passRepeat = forms.CharField()