from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserCreationForm

# Create your views here.
def homepage(request):
	# return HttpResponse("HEllo world")
	return render(request=request, template_name='registration/login.html')

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
		messages.error(request, "Unsuccessful registration. Invalid information.")

	return render (request=request, template_name="registration/login.html", context={"register_form":form})
