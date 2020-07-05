from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import EventosLista, EventoDetalle


app_name = 'Eventos'
urlpatterns = [
	url(r'^$', login_required(EventosLista.as_view()), name='Eventos_Lista'),
    url(r'^detalle_evento/(?P<pk>[0-9]+)/$', login_required(EventoDetalle.as_view()), name='Evento_Detalle'),
]