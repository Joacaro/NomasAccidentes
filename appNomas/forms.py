from django import forms
from django.db.models import fields
from .models import Cliente,Contrato

class PostForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
        fields = ('rut', 'nombres','direccion','password','correo','telefono')  
          
class LoginPostForm(forms.ModelForm):    
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
        fields = ('rut','password')

class postcontrato(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ('descripcion','fecha','firmaCli','firmaEmp')
