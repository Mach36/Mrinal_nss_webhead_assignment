import re
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='main:register')
def homepage(request):
	# return HttpResponse("HEllo world")
	return redirect('main:welcome')

def register_request(request):
	form = UserCreationForm()
	if request.method == "POST":

		form = UserCreationForm(request.POST)
		email = request.POST.get('email')
		username = request.POST.get("username")
		
		if form.is_valid():
			# print(form)
			user = form.save()
			# login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:register")
		messages.error(request,form.errors)

	return render (request=request, template_name="registration/login.html", context={"register_form":form})

def login_page(request):

	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("main:welcome")

		else:
			render(request,template_name='registration/login.html')
			messages.error(request,"Invalid Credentials")
	
	return redirect('main:register')
@login_required(login_url= '../login')
def welcome(request):

	return render(request,template_name='welcome.html',context={"user":request.user})

def logout_user(request):

	logout(request)
	return redirect('main:login')