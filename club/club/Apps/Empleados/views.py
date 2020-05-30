from django.shortcuts import HttpResponseRedirect, redirect
from django.views.generic import TemplateView, DetailView, ListView, RedirectView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator 
from django_pdfkit.views import PDFView
from .forms import EmpleadoForm, ConsultaForm
from .models import Empleado
# Create your views here.

class home(TemplateView):
	login_required = True
	template_name = 'Empleados/index.html'

	# @method_decorator(login_required)
	# def dispatch(self, request, *args, **kwargs):
	# 	return super(self.__class__, self).dispatch(request, *args, **kwargs)

class registro(FormView):
	login_required = True
	model = Empleado
	form_class =  EmpleadoForm
	template_name = 'Empleados/crear-cuenta.html'
	success_url = reverse_lazy('Empleados:home')

	# @method_decorator(login_required)
	# def dispatch(self, request, *args, **kwargs):
	# 	return super(self.__class__, self).dispatch(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			empl = self.model()
			empl.CI   = form.cleaned_data['CI']
			empl.Apellidos = form.cleaned_data['Apellidos']
			empl.Nombres = form.cleaned_data['Nombres']
			empl.Departamento = form.cleaned_data['Departamento']
			empl.Carga_Familiar = form.cleaned_data['Carga_Farmiliar']
			empl.Numero_Personal = form.cleaned_data['Numero_Personal']
			empl.FechaNacimiento = form.cleaned_data['FechaNacimiento']
			empl.Sexo = form.cleaned_data['Sexo']
			empl.Correo = form.cleaned_data['Correo']
			empl.Foto = form.cleaned_data['Foto']
			empl.save()
			return HttpResponseRedirect(reverse('Empleados:home'))
		else:
			return super(registro, self).post(self, request, *args, **kwargs)

	def form_valid(self, form):
		return super(registro, self).form_valid(form)

class Logout(RedirectView):
	pattern_name = 'Empleados:login'

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(Logout, self).get(request, *args, **kwargs)


class Login(FormView):
	form_class = AuthenticationForm
	template_name = 'Empleados/login.html'
	success_url = reverse_lazy('Empleados:home')

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.get_success_url())
		else:
			return super(Login, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(Login, self).form_valid(form)


class Carnet(PDFView):
	login_required = True
	model = Empleado
	template_name = 'Empleados/carnet.html'
	pdfkit_options = {
		'page-size' : 'letter',
		'encoding'  : 'UTF-8',
	}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		CI = kwargs['pk']
		empl = Empleado.objects.get(CI=CI)
		context['Empleado'] = empl
		self.filename = "%s.pdf" % empl.CI
		empl.Carnet = self.get_filename()
		empl.save()
		return context

class Consulta(FormView):
	login_required = True
	form_class = ConsultaForm
	template_name = 'Empleados/consulta.html'

	def post(self, request):
		form = self.form_class(request.POST)
		cedula = None
		if form.is_valid():
			cedula = form.cleaned_data['cedula']
		return HttpResponseRedirect('/pdf/'+cedula)
	def form_valid(self, form):
		return super(Consulta, self).form_valid(form)

class ListaEmpleados(PDFView):
	model = Empleado
	template_name = 'Empleados/reporte_empleados.html'
	paginated_by = 60

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		emplados = Empleado.objects.all()
		context['Empleados'] = emplados
		return context