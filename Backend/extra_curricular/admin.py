from django.contrib import admin
from extra_curricular.models import extra_curricular

class extra_curricularAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('type_of_exp','name', )

admin.site.register(extra_curricular)

# Register your models here.
