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
  ingrese_su_nombre_de_usuario = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control text-primary', 'palceholder': 'Nombre de usuario'})
  )
  contraseña = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control text-primary-emphasis', 'placeholder': 'ingrese una contraseña'})
  )
  repita_contraseña = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita su contraseña'})
  )