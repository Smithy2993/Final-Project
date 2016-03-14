from django.contrib import admin
from user.models import user

admin.site.register(user)

class UserAdmin(admin.ModelAdmin):
        list_per_page = 10
        list_display = ('username','student_ID')
