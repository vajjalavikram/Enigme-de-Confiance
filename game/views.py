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
	user_ = UserProfile.objects.get(user_name=request.user)
	
	
	if request.method == "POST":
		case = Case.objects.filter(num = 2).last()
		Copycat = request.POST['Pref_1']
		All_cheat = request.POST['Pref_2']
		All_cooperate = request.POST['Pref_3']
		Detective = request.POST['Pref_4']
		Grudger = request.POST['Pref_5']
		CopyKitten = request.POST['Pref_6']
		Simple = request.POST['Pref_7']
		Random = request.POST['Pref_8']

		p = {'Copycat':Copycat,'All_cheat':All_cheat,'All_cooperate':All_cooperate,'Detective':Detective,'Grudger':Grudger,'CopyKitten':CopyKitten,'Simple':Simple,'Random':Random}
		for i in p.keys():
			if p[i]==0:
				del p[i]

		
		a = {'Copycat':1,'All_cheat':2,'All_cooperate':3,'Detective':4,'Grudger':5,'CopyKitten':6,'Simple':7,'Random':8}
		

		if str(a[list(p.keys())[list(p.values()).index('1')]]) == str(case.Pref_1_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('2')]]) == str(case.Pref_2_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('3')]]) == str(case.Pref_3_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('4')]]) == str(case.Pref_4_ans):
			marks += 2
		if user_.result is None:
			user_.result = [marks]
		else:
			user_.result += [marks]
		
		user_.Score += marks
		user_.save()
		print(user_.result)
		score = user_.Score
		
		C1 = list(a.keys())[list(a.values()).index(int(case.Pref_1_ans))]
		C2 = list(a.keys())[list(a.values()).index(int(case.Pref_2_ans))]
		C3 = list(a.keys())[list(a.values()).index(int(case.Pref_3_ans))]
		C4 = list(a.keys())[list(a.values()).index(int(case.Pref_4_ans))]
		C = {1:C1,2:C2,3:C3,4:C4}
		print(C)
		
		return render(request,'game/result.html',{'Score': user_.Score, 'marks':marks, 'case':C})
	else:
		return render(request,'game/result.html',{'Score': user_.Score, 'marks':marks, 'case':C})
 

	
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

