from django.contrib import admin

from student.models import Student


class StudentAdminModel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_select_related = ['group']


admin.site.register(Student, StudentAdminModel)
