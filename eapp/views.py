from django.shortcuts import render,redirect
from django.http import HttpResponse 
from models import Post
from django.views.generic import View
from forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.contrib import messages

# Create your views here.

def index(request):
	lists=Post.objects.all().order_by("-timestamp")
	return render(request,"eapp/index.html",{'lists':lists})

def detail(request,id):
	lists=Post.objects.get(pk=id)
	return render(request,"eapp/detail.html",{'lists':lists})

class RegistrationView(View):
	form_class=RegistrationForm
	template_name='eapp/user_login_form.html'


	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():

			user=form.save(commit=False)

			#cleaned (normalized) data
			username =form.cleaned_data['username']
			password =form.cleaned_data['password']
			email=form.cleaned_data['email']
			user.set_password(password)
			user.save()
			messages.success(request,"User successfully created now logIn please")
		return render(request,self.template_name,{'form':form,})


class LoginView(View):
	form_class=LoginForm
	template_name='eapp/user_login_form.html'


	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():


			#cleaned (normalized) data
			username =form.cleaned_data['username']
			password =form.cleaned_data['password']

	

			#authenticatin

			user=authenticate(username=username,password=password)

			if user:
				pass
			else:
				messages.success(request,"Wrong password or username")
				

			if user is not None:
				if user.is_active:
						login(request,user)
						lists=Post.objects.all().order_by("-timestamp")
						return render(request,'eapp/index.html',{"user":user,"lists":lists})

		return render(request,self.template_name,{'form':form})


#-----log-out

def logout_view(request):
    logout(request)
    return redirect('eapp:index')


#-----------

class PostCreate(CreateView):
	model=Post
	fields=['title','image','content']