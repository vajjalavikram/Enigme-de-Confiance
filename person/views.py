from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse
# Create your views here.
def home(request):
	if not request.user.is_authenticated:
		return HttpResponse('<a href="/login">Login Here</a>')
	else:
		context = {
			'UserProfile':UserProfile.objects.filter(user_name=request.user),
		}
		return render(request,'person/home.html',context)