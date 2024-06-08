from django import forms

class ContactForm(forms.Form):
  nombre = forms.CharField(
    max_length=64,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
  email = forms.EmailField(
    label='Correo Electronico',
    widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Correo Electronico'})
    )
  mensaje = forms.CharField(
    max_length=64,
    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
)