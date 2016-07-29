from django.contrib import admin
from events.models import Event
from . import models 
# Register your models here.
from base.admin import TimeAuditAdmin

@admin.register(Event)
class EventAdmin(TimeAuditAdmin):
	#fields  = ('id','title','body','event_date','start_time','end_time','event_type_id','event_standard')
	list_display = ('id','title','body','event_date','start_time','end_time','event_type','event_standard')


#admin.site.register(Event,EventAdmin)