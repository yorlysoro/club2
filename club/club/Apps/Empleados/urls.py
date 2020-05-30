from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django_pdfkit import PDFView
from .views import home, registro, Login, Logout, Carnet, Consulta, ListaEmpleados


app_name = 'Empleados'
urlpatterns = [
	path('', Login.as_view(), name='login'),
	path('home/', login_required(home.as_view()), name='home'),
	path('registro/', login_required(registro.as_view()), name='registro'),
	path('pdf/<slug:pk>', login_required(Carnet.as_view()), name='pdf'),
	path('logout/', Logout.as_view(), name='logout'),
	path('consultar/', login_required(Consulta.as_view()), name='consultar'),
	path('reporte/', login_required(ListaEmpleados.as_view()), name='reporte'),

]

