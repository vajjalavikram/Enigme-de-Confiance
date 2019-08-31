from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, Model
from picklefield.fields import PickledObjectField

# Create your models here.


class UserProfile(models.Model):
   user_name = models.OneToOneField(User, on_delete = models.CASCADE)
   Score = models.IntegerField(blank=True, default = 0)
   result=PickledObjectField(null=True)
   num = models.IntegerField(blank = True, default = 1)
   prefs = PickledObjectField(null=True)
   

class Case(models.Model):
	
	Copy_1 = models.IntegerField(blank=True, default = 0)
	Cheat_2 = models.IntegerField(blank=True, default = 0)
	Coop_3 = models.IntegerField(blank=True, default = 0)
	Detective_4 = models.IntegerField(blank=True, default = 0)
	CopyKit_5 = models.IntegerField(blank=True, default = 0)
	Simp_6 = models.IntegerField(blank=True, default = 0)
	Random_7 = models.IntegerField(blank=True, default = 0)
	Grudger_7 = models.IntegerField(blank=True, default = 0)
	Points_both_co_op = models.IntegerField(blank=True, default = 2)
	Points_both_cheat = models.IntegerField(blank=True, default = 0)
	Points_one_cheat = models.IntegerField(blank=True, default = 3)
	Points_one_coop = models.IntegerField(blank=True, default = -1)
	No_of_games = models.IntegerField(blank=True, default = 10)
	Error = models.IntegerField(blank=True, default = 0)
	Pref_1_ans = models.IntegerField(blank=True, default = 0)
	Pref_2_ans = models.IntegerField(blank=True, default = 0)
	Pref_3_ans = models.IntegerField(blank=True, default = 0)
	Pref_4_ans = models.IntegerField(blank=True, default = 0)
	flag = models.IntegerField(blank=True,default = 0)
	num_eliminate = models.IntegerField(blank=True, default = 0)

