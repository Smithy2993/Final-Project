from django.contrib import admin
from student.models import student



class StudentAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('first_name','middle_name','last_name')

admin.site.register(student, StudentAdmin)
