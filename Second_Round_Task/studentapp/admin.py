from django.contrib import admin
from .models import Studentinfo,StudentAcademics

@admin.register(Studentinfo)
class StudentinfoAdmin(admin.ModelAdmin):
    list_display=['roll_no','name','clas','school','mobile']

@admin.register(StudentAcademics)
class StudentAcadAdmin(admin.ModelAdmin):
    list_display=['stu_acad_id','roll_no_id']

