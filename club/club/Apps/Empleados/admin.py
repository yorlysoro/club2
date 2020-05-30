from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

# Register your models here.

from .models import Empleado
admin.site.site_header = "Administracion Club Kilovatico"
admin.site.site_title = "Area de Administracion | Club Kilovatico"
admin.site.index_title = "Bienvenido al area de administracion del Club Kilovatico"


class EmpleadoAdmin(admin.ModelAdmin):
#	actions = ['Imprimir'] 
	list_display = ('cedula', 'Nombres', 'Apellidos', 'carnet')
	show_full_result_count = True

	def cedula(self, obj):
		return "%s" % (obj.CI)



admin.site.register(Empleado, EmpleadoAdmin)
