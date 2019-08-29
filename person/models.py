from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, Model


# Create your models here.


class UserProfile(models.Model):
   user_name = models.OneToOneField(User, on_delete = models.CASCADE)
   Name_1 = models.CharField(max_length=256, blank=True, null=True)
   Name_2 = models.CharField(max_length=256, blank=True, null=True)
   Score = models.IntegerField(blank=True, default = 0)
   
class Case(models.Model):
	num = models.IntegerField(blank = True, default = 1)
	Char_1 = models.IntegerField(blank=True, default = 0)
	Char_2 = models.IntegerField(blank=True, default = 0)
	Char_3 = models.IntegerField(blank=True, default = 0)
	Char_4 = models.IntegerField(blank=True, default = 0)
	Char_5 = models.IntegerField(blank=True, default = 0)
	Char_6 = models.IntegerField(blank=True, default = 0)
	Char_7 = models.IntegerField(blank=True, default = 0)
	Char_8 = models.IntegerField(blank=True, default = 0)
	Char_9 = models.IntegerField(blank=True, default = 0)
	Char_10 = models.IntegerField(blank=True, default = 0)
	Char_11 = models.IntegerField(blank=True, default = 0)
	Char_12 = models.IntegerField(blank=True, default = 0)
	Char_13 = models.IntegerField(blank=True, default = 0)
	Char_14 = models.IntegerField(blank=True, default = 0)
	Char_15 = models.IntegerField(blank=True, default = 0)
	Char_16 = models.IntegerField(blank=True, default = 0)
	Char_17 = models.IntegerField(blank=True, default = 0)
	Char_18 = models.IntegerField(blank=True, default = 0)
	Char_19 = models.IntegerField(blank=True, default = 0)
	Char_20 = models.IntegerField(blank=True, default = 0)
	Char_21 = models.IntegerField(blank=True, default = 0)
	Char_22 = models.IntegerField(blank=True, default = 0)
	Char_23 = models.IntegerField(blank=True, default = 0)
	Char_24 = models.IntegerField(blank=True, default = 0)
	Char_25 = models.IntegerField(blank=True, default = 0)
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