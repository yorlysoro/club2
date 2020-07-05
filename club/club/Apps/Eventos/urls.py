from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import EventosLista


app_name = 'Eventos'
urlpatterns = [
	url(r'^$', login_required(EventosLista.as_view()), name='Eventos_Lista'),

]