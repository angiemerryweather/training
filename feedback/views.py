from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from feedback.models import Attendee
from feedback.forms import AttendeeForm

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/index.html', {}, context)
	
def add_feedback(request):
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'POST':
		attendee_form = AttendeeForm(request.POST)
		
		if attendee_form.is_valid():
			attendee_obj = attendee_form.save(commit=False)
			#attendee_obj.company_id = 1
			#attendee_obj.role_id = 1
			attendee_obj.save()
			return HttpResponseRedirect('/feedback/')
		else:
			return HttpResponse(attendee_form.errors)
	else:
		form = AttendeeForm()
	
	return render_to_response('feedback/add_feedback.html', {'form': form}, context)
