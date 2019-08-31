from django.shortcuts import render,redirect
from person.models import Case, UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User

def play(request):
	user=UserProfile.objects.filter(user_name=request.user).first()
	case = Case.objects.filter(id=user.num).first()
	
	if case is None:
		return redirect('/result')
	#case.num += 1
	context = {'Copy':case.Copy_1,'Cheat':case.Cheat_2,'Coop':case.Coop_3,'Detect':case.Detective_4,'Grudge':case.Grudger_7,'CopyKit':case.CopyKit_5,'Simple':case.Simp_6,'Random':case.Random_7}
	if case.id >= 1 and case.id <= 8:
		return render(request,'game/index.html',context)
	else:
		return render(request,'game/thank.html',context)

def result(request):

	user_ = UserProfile.objects.get(user_name=request.user)
	
	
	if request.method == "POST":
		marks = 0 
		case = Case.objects.filter(id=user_.num).first()

		a = {'Copycat':1,'All_cheat':2,'All_cooperate':3,'Detective':4,'Grudger':5,'CopyKitten':6,'Simple':7,'Random':8}
		C1 = list(a.keys())[list(a.values()).index(int(case.Pref_1_ans))]
		C2 = list(a.keys())[list(a.values()).index(int(case.Pref_2_ans))]
		C3 = list(a.keys())[list(a.values()).index(int(case.Pref_3_ans))]
		C4 = list(a.keys())[list(a.values()).index(int(case.Pref_4_ans))]

		ans = {1:'Copycat',2:'All_cheat',3:'All_cooperate',4:'Detective',5:'Grudger',6:'CopyKitten',7:'Simple',8:'Random'}

		C = {1:C1,2:C2,3:C3,4:C4}

		Copycat = request.POST['Pref_1']
		All_cheat = request.POST['Pref_2']
		All_cooperate = request.POST['Pref_3']
		Detective = request.POST['Pref_4']
		Grudger = request.POST['Pref_5']
		CopyKitten = request.POST['Pref_6']
		Simple = request.POST['Pref_7']
		Random = request.POST['Pref_8']

		p = {'Copycat':Copycat,'All_cheat':All_cheat,'All_cooperate':All_cooperate,'Detective':Detective,'Grudger':Grudger,'CopyKitten':CopyKitten,'Simple':Simple,'Random':Random}
	

		for key in list(p.keys()):
			if p[key] == '0':
				p.pop(key)

		if str(a[list(p.keys())[list(p.values()).index('1')]]) == str(case.Pref_1_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('2')]]) == str(case.Pref_2_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('3')]]) == str(case.Pref_3_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('4')]]) == str(case.Pref_4_ans):
			marks += 4
		if user_.result is None:
			user_.result = [marks]
		else:
			user_.result += [marks]
		
		print(str(a[list(p.keys())[list(p.values()).index('1')]]) +" "+ str(case.Pref_1_ans))
		user_.Score += marks
		user_.num += 1
		user_.prefs = p
		print(str(marks) + " " + str(user_.Score))
		user_.save()
		score = user_.Score
		
	case = Case.objects.filter(id = user_.num - 1).first()	
	a = {'Copycat':1,'All_cheat':2,'All_cooperate':3,'Detective':4,'Grudger':5,'CopyKitten':6,'Simple':7,'Random':8}
	C1 = list(a.keys())[list(a.values()).index(int(case.Pref_1_ans))]
	C2 = list(a.keys())[list(a.values()).index(int(case.Pref_2_ans))]
	C3 = list(a.keys())[list(a.values()).index(int(case.Pref_3_ans))]
	C4 = list(a.keys())[list(a.values()).index(int(case.Pref_4_ans))]

	ans = {1:'Copycat',2:'All_cheat',3:'All_cooperate',4:'Detective',5:'Grudger',6:'CopyKitten',7:'Simple',8:'Random'}

	C = {1:C1,2:C2,3:C3,4:C4}

	sorted_x = sorted((user_.prefs).items(), key=lambda kv: kv[1])
	list_pref_sent = []
	for x in sorted_x:
		list_pref_sent.append(x[0])

	list_ans = []
	list_ans.append(ans[case.Pref_1_ans])
	list_ans.append(ans[case.Pref_2_ans])
	list_ans.append(ans[case.Pref_3_ans])
	list_ans.append(ans[case.Pref_4_ans])
	# print(user_.result[0])
	return render(request,'game/result.html',{'hut': user_.num - 1,'Score': user_.Score, 'marks':user_.result[user_.num - 1], 'case':list_ans, 'prefs': list_pref_sent})
 

	
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

