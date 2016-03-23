# extra_curricular admin.py

#Import necessary functions
from django.contrib import admin
from extra_curricular.models import extra_curricular

# extra_curricular admin model
#Displays the data in the table
class extra_curricularAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('type_of_exp','name', )

#Register the extra_curricular model
admin.site.register(extra_curricular)

