from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm


# Create your views here.




def display(request):
	return render(request,"users/display.html")



def register(request):
	if request.method=="GET":
		return render(request,"users/register.html",{"form":CustomUserCreationForm})
	elif request.method=="POST":
		form=CustomUserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect(reverse("display"))



def setcookie(request):
	x=HttpResponse("my cookie")
	x.set_cookie('cookie_name','created cookie',max_age=None)
	return x

def showcookie(request):
	s=request.COOKIES['cookie_name']
	return HttpResponse(s)

def create_session(request):
	request.session['name']='my session'
	request.session['name1']="session2"
	return HttpResponse("<h2>Session created </h2>")


def get_session(request):
	response="<h1>Sesion</h1>"
	if request.session.get('name'):
		response=response+"name:{0} <br>".format(request.session.get('name'))
	if request.session.get('name'):
		response=response+"name:{0} <br>".format(request.session.get('name1'))
		return HttpResponse(response)
	else:
		return redirect('setsession')
