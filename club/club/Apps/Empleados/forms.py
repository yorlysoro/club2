from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import DEPARTAMENTO_CHOICES

class EmpleadoForm(forms.Form):
	CI = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'name'	: 'cedula',
		'minlength' : '7',
		'maxlength' : '8',
		'placeholder' : 'Ingrese su Cedula',
		'type' : 'text'
		}))
	Apellidos = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'name'	: 'apellido',
		'placeholder' : 'Ingrese su Apellido',
		'type' : 'text'
		}))
	Nombres = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'name'	: 'nombre',
		'placeholder' : 'Ingrese su Nombre',
		'type' : 'text'
		}))
	Departamento = forms.ChoiceField(required=True, label=('Seleccione su gerencia'), choices=DEPARTAMENTO_CHOICES, widget=forms.Select(attrs={
		'class' : 'form-control',
		'name'	: 'Departamento',
		'type' : 'text'
		}))
	Carga_Farmiliar = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'name'	: 'Carga_Farmiliar',
		'placeholder' : 'Ingrese su carga familiar',
		'type' : 'number',
		'min_value' : '0',
		'max_value' : '10'
		}))
	FechaNacimiento = forms.DateField(required=True,widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'id'    : 'usr1',
		'autocomplete' : 'off',
		'name'	: 'event_date',
		'placeholder' : 'DIA/MES/AÑO',
		'type' : 'text'
		}), label=('Fecha de nacimiento'))
	Numero_Personal = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'id'    : 'Numero_Personal',
		'name'	: 'Numero_Personal',
		'placeholder' : 'Ingrese su codigo de trabajador',
		'type' : 'text'
		}))
	sexo = [
		('M' , 'Masculino'),
		('F' , 'Femenino'),
	]
	Sexo = forms.ChoiceField(required=True, label=('Seleccione su Sexo'), choices=sexo, widget=forms.Select(attrs={
		'class' : 'form-control',
		'id'    : 'Sexo',
		'name'	: 'Sexo'
		}))
	Correo = forms.EmailField(required=False, widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'id'    : 'usr1',
		'name'	: 'event_date',
		'placeholder' : 'Ingrese su Correo Electronico',
		'type' : 'email'
		}) )
	Foto = forms.ImageField(required=True, label=('Seleccione cargue su foto'), widget=forms.FileInput(attrs={
		'type' : 'file',
		'name' : 'avatar'
		}))

class ConsultaForm(forms.Form):
	cedula = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'name'	: 'cedula',
		'minlength' : '7',
		'maxlength' : '8',
		'placeholder' : 'Ingrese su Cedula',
		'type' : 'text'
		}))


class FormularioLogin(AuthenticationForm):
	def __init__(self, *args, **kwargs):
	    super(FormularioLogin, self).__init__(*args,**kwargs)
	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['username'].widget.attrs['placeholder'] = 'Coloque su Usuario...'
	    self.fields['password'].widget.attrs['class'] = 'form-control'
	    self.fields['password'].widget.attrs['placeholder'] = 'Coloque su contraseña...'