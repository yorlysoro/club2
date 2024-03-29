from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^', include('club.Apps.Empleados.urls')),
	url(r'^eventos/', include('club.Apps.Eventos.urls')),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
	url(r'^admin/', admin.site.urls),
	
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)