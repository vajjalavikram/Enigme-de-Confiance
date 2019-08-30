from django.shortcuts import render
from person.models import Case, UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User
def play(request):
	
	case = Case.objects.filter(num = 1).first()
	case.num += 1
	case.save()
	context = {'Copy':case.Copy_1,'Cheat':case.Cheat_2,'Coop':case.Coop_3,'Detect':case.Detective_4,'Grudge':case.Grudger_7,'CopyKit':case.CopyKit_5,'Simple':case.Simp_6,'Random':case.Random_7}
	return render(request,'game/index.html',context)

def result(request):
	marks = 0 
	case = Case.objects.filter(num = 2).last()
	Copycat = request.POST.get('Pref_1')
	All_cheat = request.POST.get('Pref_2')
	All_cooperate = request.POST.get('Pref_3')
	Detective = request.POST.get('Pref_4')
	Grudger = request.POST.get('Pref_5')
	Copykitten = request.POST.get('Pref_6')
	Simpleton = request.POST.get('Pref_7')
	Random = request.POST.get('Pref_8')
	p = {'Copycat':Copycat,'All_cheat':All_cheat,'All_cooperate':All_cooperate,'Detective':Detective,'Grudger':Grudger,'CopyKitten':CopyKitten,'Simple':Simple,'Random':Random}
	for i in range(len(p)):
		if p[i]==None:
			del p[i]


	a = {'Copycat':1,'All_cheat':2,'All_cooperate':3,'Detective':4,'Grudger':5,'Copykitten':6,'Simpleton':7,'Random':8}
	

	if str(a(p.keys()[p.values().index(1)])) == str(case.Pref_1_ans):
		marks += 4
	if str(a(p.keys()[p.values().index(2)])) == str(case.Pref_2_ans):
		marks += 4
	if str(a(p.keys()[p.values().index(3)])) == str(case.Pref_3_ans):
		marks += 4
	if str(a(p.keys()[p.values().index(4)])) == str(case.Pref_4_ans):
		marks += 2
	user_ = UserProfile.objects.get(user_name=request.user)
	if user_.result is None:
		user_.result = [marks]
	else:
		user_.result += [marks]
	print(user_.result)
	user_.Score += marks
	user_.save()
	score = user_.Score
	prefs = [P1,P2,P3,P4]
	C1 = analog[str(case.Pref_1_ans)]
	C2 = analog[str(case.Pref_2_ans)]
	C3 = analog[str(case.Pref_3_ans)]
	C4 = analog[str(case.Pref_4_ans)]
	C = [C1,C2,C3,C4]
	return render(request,'game/result.html',{'Score': score, 'marks':marks, 'case':C, 'prefs':prefs})
 

	
def play_words(request):
	return render(request,'game/words.html')


def modal(request):
	return render(request,'game/modal.html')

# def dbupdate(request):

# 	user_ = User.objects.all()
# 	for one in user_:
# 		one.is_staff = True
# 		one.save()
# 	return HttpResponse()

