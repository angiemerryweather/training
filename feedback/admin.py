from django.contrib import admin
from feedback.models import Answer, Attendee, AnswerOffered, Company, Form, Question, Role, TrainingType
from feedback.forms import AttendeeForm


class TrainingTypeAdmin(admin.ModelAdmin):
	pass

class AnswerAdmin(admin.ModelAdmin):
	list_display = (
		'answer_id',
		'answer_offered',
		'answer_text',
		'form'
	)
	readonly_fields = ['form']
	
class AnswerOfferedAdmin(admin.ModelAdmin):
	list_display = ('answer_offered_id', 'answer_text')
	ordering = ('answer_offered_id',)
	fields = ['answer_text']
	
class AttendeeInline(admin.StackedInline):
	model = Attendee
	
class AttendeeAdmin(admin.ModelAdmin):
	list_display = ('attendee_id',
					'first_name',
				 	'last_name',
				 	'company',
				 	'role',
				 	'created')
				 	
	fields = ['first_name', 
			  'last_name', 
			  'email',
			  'phone_number', 
			  'sex', 
			  'experience',
			  'company',
			  'role']
			  
	def __init__(self, model, admin_site):
		super(AttendeeAdmin, self).__init__(model, admin_site)
		self.form.admin_site = admin_site # capture admin site
				 	
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name', 'industry', 'postcode')
	inlines = [AttendeeInline,]
	
class FormAdmin(admin.ModelAdmin):
	list_display = ('attendee', 'training_type','training_date')
	fields = ['attendee', 'training_type', 'training_date']
	readonly_fields = ['training_date']
	
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_id', 'question')
	fields = ['question']
	
class RoleAdmin(admin.ModelAdmin):
	
	def __init__(self, model, admin_site):
		super(RoleAdmin, self).__init__(model, admin_site)
		self.form.admin_site = admin_site # capture admin site

# Register your models here.
admin.site.register(Answer, AnswerAdmin)
admin.site.register(AnswerOffered, AnswerOfferedAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(TrainingType)
