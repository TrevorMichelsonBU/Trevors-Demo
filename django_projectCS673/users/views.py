from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request): #class that will turn to html
	if request.method == 'POST': #verify it's a post request
		form = UserRegisterForm(request.POST) #request.POST is the data we received from the post
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been Created!') #flash message
			return redirect('blog-home')
	else:
		form = UserRegisterForm() #if it's not a post request, we return a blank form
	return render(request, 'users/register.html', {'form': form})


@login_required #Adds functionality to profiler. Forces user to be logged in to access the below
def profile(request): 
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user) #instance is pulling current user's info
		p_form = ProfileUpdateForm(request.POST, 
			request.FILES, 
			instance=request.user.profile)	#instance is pulling current user's profile
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account has been Updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)