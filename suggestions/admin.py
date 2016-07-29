from django.contrib import admin

from base.admin import TimeAuditAdmin
# Register your models here.
from . import models



@admin.register(models.Suggestion)
class SuggestionAdmin(TimeAuditAdmin):
	list_display = ('title','body','against_id','anonymous','assignedTo')
