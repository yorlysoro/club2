from django.contrib import admin

# Register your models here.

from .models import Empleado
admin.site.site_header = "Administracion Club Kilovatico"
admin.site.site_title = "Area de Administracion | Club Kilovatico"
admin.site.index_title = "Bienvenido al area de administracion del Club Kilovatico"


class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('cedula', 'Nombres', 'Apellidos', 'carnet')
	show_full_result_count = True

	def cedula(self, obj):
		return "%s" % (obj.CI)



admin.site.register(Empleado, EmpleadoAdmin)
