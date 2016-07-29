from django.contrib import admin
from base.admin import TimeAuditAdmin
# Register your models here.
from . import models



@admin.register(models.Complaint)
class ComplaintAdmin(TimeAuditAdmin):
	list_display = ('title','body','category_id','against_id','anonymous','status','assignedTo')





