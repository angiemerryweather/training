from django.contrib import admin
from feedback.models import Attendee, Company, Role, TrainingType


class TrainingTypeAdmin(admin.ModelAdmin):
	pass
	
class AttendeeAdmin(admin.ModelAdmin):
	list_display = ('first_name',
				 	'last_name',
				 	'company',
				 	'role',
				 	'created')
				 	
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name', 'industry', 'postcode')

# Register your models here.
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Role)
admin.site.register(TrainingType)