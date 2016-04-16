#student admin.py

# Import admin and the student model
from django.contrib import admin
from student.models import student
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse

#Export the student user model
def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mystudentmodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Username"),
        smart_str(u"Student ID"),
        smart_str(u"First Name"),
        smart_str(u"Middle Name"),
        smart_str(u"Last Name"),
        smart_str(u"Gender"),
        smart_str(u"Year"),
        smart_str(u"Degree"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.user),
            smart_str(obj.student_ID),
            smart_str(obj.first_name),
            smart_str(obj.middle_name),
            smart_str(obj.last_name),
            smart_str(obj.gender),
            smart_str(obj.year),
            smart_str(obj.degree),
        ])
    return response
export_csv.short_description = u"Export CSV"


# Specify how the records will be displayed in the table
class StudentAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('first_name','middle_name','last_name')
        actions = [export_csv]

#Upload image with users student ID appended as name
def update_filename(instance, filename):
    path = "upload/path/"
    format = student.student_ID + instance.file_extension
    return os.path.join(path, format)

#Register the student model along with the admin preferences
admin.site.register(student, StudentAdmin)

