#student admin.py

# Import admin and the student model
from django.contrib import admin
from student.models import student


# Specify how the records will be displayed in the table
class StudentAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('first_name','middle_name','last_name')

#Register the student model along with the admin preferences
admin.site.register(student, StudentAdmin)
