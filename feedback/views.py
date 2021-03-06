from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from feedback.models import Answer, AnswerOffered, Attendee, Form, Question
from feedback.forms import AttendeeForm, QuestionForm
from django.utils.timezone import now

# View helper functions
def get_offered_answers():
	answers = AnswerOffered.objects.all()
	return answers

def get_questions():
	questions = Question.objects.all()
	return questions
	
def create_form(context_dict):
	new_form = Form()
	new_form.attendee = context_dict['attendee']
	new_form.training_type = context_dict['question_form'].cleaned_data.get('training_type')
	new_form.training_date = context_dict['question_form'].cleaned_data.get('training_date')
	new_form.save()
	return new_form
	
def add_answer_to_form(q_id, form, ans):	
	"""
	Adds answer model instances to the appropriate form.
	
	Arguments:
	q_id -- ID of the question being answered
	form -- form the answer should be attached to
	ans  -- each answer captured in QuestionForm
	"""
	
	new_answer = Answer()
	new_answer.question = Question.objects.get(question_id=q_id)
	new_answer.form = form
	
	""" Differentiates between Likert scale answers and free text """
	
	if ans.isdigit():
		new_answer.answer_offered = AnswerOffered.objects.get(answer_offered_id=ans)
	else:
		# check whether it was filled in, if not set N/A
		if not ans:
			ans = 'N/A'
		new_answer.answer_offered = AnswerOffered.objects.get(answer_offered_id=6)
		new_answer.answer_text = ans
	
	new_answer.save()
	
	
# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/index.html', context_dict, context)
	
def add_attendee(request):
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'POST':
		attendee_form = AttendeeForm(request.POST)
		# check form is valid then save to DB
		if attendee_form.is_valid():
			attendee_obj = attendee_form.save(commit=False)
			attendee_obj.save()
			context_dict['attendee'] = attendee_obj
			# redirect to questions page and pass ID of new attendee
			return HttpResponseRedirect('/feedback/questions/%s/' % attendee_obj.attendee_id)
		else:
			return HttpResponse(attendee_form.errors)
	else:
		a_form = AttendeeForm()
	
	context_dict['a_form'] = a_form
	return render_to_response('feedback/add_attendee.html', context_dict, context)
	
	
def new_form(request, attendee_id):
	"""
	Processes feedback form, creating multiple Model instances.
	"""
	context = RequestContext(request)
	context_dict = {}
	# grab new attendee from url
	attendee = get_object_or_404(Attendee, pk=attendee_id) 
	
	# set up context_dict with required objects
	context_dict['attendee'] = attendee
	
	# displaying the form
	if request.method == 'POST':
		question_form = QuestionForm(request.POST)
		if question_form.is_valid():
		
			# add the form to context_dict
			context_dict['question_form'] = question_form
			
			# then create a new form and add to context
			context_dict['created_form'] = create_form(context_dict)
			
			# now create new answers attached to the form
			add_answer_to_form(1, context_dict['created_form'], question_form.cleaned_data.get('q1'))
			add_answer_to_form(2, context_dict['created_form'], question_form.cleaned_data.get('q2'))
			add_answer_to_form(3, context_dict['created_form'], question_form.cleaned_data.get('q3'))
			add_answer_to_form(4, context_dict['created_form'], question_form.cleaned_data.get('q4'))
			add_answer_to_form(5, context_dict['created_form'], question_form.cleaned_data.get('q5'))
			add_answer_to_form(6, context_dict['created_form'], question_form.cleaned_data.get('q6'))
			add_answer_to_form(7, context_dict['created_form'], question_form.cleaned_data.get('q7'))
			add_answer_to_form(8, context_dict['created_form'], question_form.cleaned_data.get('q8'))
			add_answer_to_form(9, context_dict['created_form'], question_form.cleaned_data.get('q9'))
			# display form
			return HttpResponseRedirect('/feedback/')
		else:
			return HttpResponse(question_form.errors)
	else:
		question_form = QuestionForm()
	context_dict['question_form'] = question_form
	
	return render_to_response('feedback/questions.html', context_dict, context)
