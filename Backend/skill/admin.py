# skill admin.py

# Import admin and skill model
from django.contrib import admin
from skill.models import skill
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse

#Export the skills user model
def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=myskillsmodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Student ID"),
        smart_str(u"Name"),
        smart_str(u"Additional Skills"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.student_ID),
            smart_str(obj.name),
            smart_str(obj.additional),
        ])
    return response
export_csv.short_description = u"Export CSV"

class skillsAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('student_ID','name','additional' )
        actions = [export_csv]

#Register skill model
admin.site.register(skill, skillsAdmin)
