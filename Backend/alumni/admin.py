#Alumni admin.py

#Import the admin functionality along with the alumni model
from django.contrib import admin
from alumni.models import alumni

class AlumniAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('first_name', 'last_name', 'course', 'faculty')

#Registering the models with the django database. This will allow records to be added to the database
admin.site.register(alumni, AlumniAdmin)

