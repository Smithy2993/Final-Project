# extra_curricular admin.py

#Import necessary functions
from django.contrib import admin
from extra_curricular.models import extra_curricular
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse

#Export the experience user model
def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=myexperiencemodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Student ID"),
        smart_str(u"Type of Experience"),
        smart_str(u"Name of Company"),
        smart_str(u"Role"),
        smart_str(u"Start Date"),
        smart_str(u"End Date"),
        smart_str(u"Location"),
        smart_str(u"Description"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.student_ID),
            smart_str(obj.type_of_exp),
            smart_str(obj.name),
            smart_str(obj.role),
            smart_str(obj.start_date),
            smart_str(obj.end_date),
            smart_str(obj.Location),
            smart_str(obj.Description),
        ])
    return response
export_csv.short_description = u"Export CSV"

# extra_curricular admin model
#Displays the data in the table
class extra_curricularAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('student_ID','type_of_exp','name','role' )
        actions = [export_csv]

#Register the extra_curricular model
admin.site.register(extra_curricular, extra_curricularAdmin)

