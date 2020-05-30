from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import home, registro, Login, Logout, Carnet, Consulta, ListaEmpleados


app_name = 'Empleados'
urlpatterns = [
	url(r'^$', Login.as_view(), name='login'),
	url(r'^home/$', login_required(home.as_view()), name='home'),
	url(r'^registro/$', login_required(registro.as_view()), name='registro'),
	url(r'^(?P<Empleado_CI>[0-9]+)/pdf/$', login_required(Carnet.as_view()), name='pdf'),
	url(r'^logout/$', Logout.as_view(), name='logout'),
	url(r'^consultar/$', login_required(Consulta.as_view()), name='consultar'),
	url(r'^reporte/$', login_required(ListaEmpleados.as_view()), name='reporte'),

]

