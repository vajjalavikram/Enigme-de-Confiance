from django.shortcuts import render
from person.models import Case, UserProfile

def play(request):
	
	case = Case.objects.filter(num = 1).first()
	case.num += 1
	case.save()
	context = {'Copy':case.Copy_1,'Cheat':case.Cheat_2,'Coop':case.Coop_3,'Detect':case.Detective_4,'Grudge':case.Grudger_7,'CopyKit':case.CopyKit_5,'Simple':case.Simp_6,'Random':case.Random_7}
	return render(request,'game/index.html',context)

def result(request):
	marks = 0 
	case = Case.objects.filter(num = 2).last()
	Pref1 = request.POST['Pref_1']
	Pref2 = request.POST['Pref_2']
	Pref3 = request.POST['Pref_3']
	Pref4 = request.POST['Pref_4']
	analog = {'1':'Copycat','2':'All cheat','3':'All cooperate','4':'Detective','5':'Grudger','6':'Copykitten','7':'Simpleton','8':'Random'}
	P1 = analog[str(Pref1)]
	P2 = analog[str(Pref2)]
	P3 = analog[str(Pref3)]
	P4 = analog[str(Pref4)]

	if str(Pref1) == str(case.Pref_1_ans):
		marks += 10
	if str(Pref2) == str(case.Pref_2_ans):
		marks += 8
	if str(Pref3) == str(case.Pref_3_ans):
		marks += 6
	if str(Pref4) == str(case.Pref_4_ans):
		marks += 4
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