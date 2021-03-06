# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
import datetime

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey('Question')
    form = models.ForeignKey('Form')
    answer_offered = models.ForeignKey('AnswerOffered')
    answer_text = models.CharField(max_length=1000)
    class Meta:
        managed = False
        db_table = 'answer'

class AnswerOffered(models.Model):
    answer_offered_id = models.IntegerField(primary_key=True)
    answer_text = models.CharField(max_length=45)
    
    def __unicode__(self):
    	return self.answer_text
    
    class Meta:
        db_table = 'answer_offered'
        verbose_name_plural = 'offered answers'

class Attendee(models.Model):
    attendee_id = models.AutoField(primary_key=True)
    company = models.ForeignKey('Company')
    role = models.ForeignKey('Role')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=45, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True, null=True)
    experience = models.CharField(max_length=5)
    
    def __unicode__(self):
    	full_name = self.first_name + ' ' + self.last_name
    	return full_name
    class Meta:
        db_table = 'attendee'

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    industry = models.CharField(max_length=20, blank=True)
    address_1 = models.CharField(max_length=30, blank=True)
    address_2 = models.CharField(max_length=30, blank=True)
    town_city = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    
    def __unicode__(self):
    	return self.name
    class Meta:
        managed = False
        db_table = 'company'
        verbose_name_plural = 'companies'

class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    attendee = models.ForeignKey('Attendee')
    training_type = models.ForeignKey('TrainingType')
    training_date = models.DateField()
    
    def __unicode__(self):
    	# Joe Bloggs - TouchStar Intermediate (01/02/2014)
    	f = self.attendee.__unicode__() + ' - ' + self.training_type.__unicode__() + ' (' + self.training_date.__str__() + ')'
    	return f
    
    class Meta:
        db_table = 'form'

class FormQuestionAnswer(models.Model):
    form_id = models.IntegerField()
    question_id = models.IntegerField()
    answer_offered_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'form_question_answer'

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=45)
    
    def __unicode__(self):
    	return self.question
    
    class Meta:
        managed = False
        db_table = 'question'

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=45)
    technical = models.CharField(max_length=1)
    
    def __unicode__(self):
    	return self.job_title
    	
    class Meta:
        managed = False
        db_table = 'role'

class TrainingType(models.Model):
    training_type_id = models.IntegerField(primary_key=True)
    training_type_desc = models.CharField(max_length=45)
    
    def __unicode__(self):
    	return self.training_type_desc
    class Meta:
        managed = False
        db_table = 'training_type'

# -- Django admin tables
class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        
class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'


class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'
