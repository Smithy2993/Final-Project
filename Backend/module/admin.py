from django.contrib import admin
from module.models import module

class ModuleAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('student_ID', 'name','credits','results')

admin.site.register(module, ModuleAdmin)

# Register your models here.
