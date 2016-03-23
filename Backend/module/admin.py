#module admin.py

# Import module model aswell as admin capabilities
from django.contrib import admin
from module.models import module

# Module admin class
# Lists specified data within the django database
class ModuleAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('student_ID', 'name','credits','results')

#Register the module model
admin.site.register(module, ModuleAdmin)

