from django.contrib import admin
from homework.models import Homework
from base.admin import TimeAuditAdmin,AuditAdmin 
from . import models
# Register your models here.


@admin.register(models.Homework)
class HomeworkAdmin(TimeAuditAdmin):
	pass
	#fields = ('homework','subjectID','standardId','teacherId','lastdate')
	#list_display = ('homework','subjectID','standardId','teacherId','lastdate')+TimeAuditAdmin.list_display
#admin.site.register(Homework, HomeworkAdmin)