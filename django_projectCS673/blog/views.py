from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Post, Menu #can use .models because it's in same directory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #class based views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def home(request): #Request has to be there
	context = {
		'posts': Post.objects.all() 
	}
	return render(request, 'blog/home.html', context) #second arg is template name

class PostListView(ListView):
	model = Post #Post is a class which has all the info for all our many Posts, which then get sent to the .html to actually display
	template_name = 'blog/home.html' # PostListView in url.py is looking for this: <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3 #number of posts per page

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' # Username will be specified into this
	context_object_name = 'posts'
	#ordering = ['-date_posted']
	paginate_by = 3 #number of posts per page

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username')) #checks to see if exist or 404
		return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView): #login required mixin forced you to login before posting
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user #the form we're trying to submit is equal to the current logged in user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #login required mixin forced you to login before posting, userpasesstest makes sure you're the user of post
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user #the form we're trying to submit is equal to the current logged in user
		return super().form_valid(form)

	def test_func(self): #checks to make sure current author
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'}) 

### MENUS ###
class MenuCreateView(LoginRequiredMixin, CreateView):
	model = Menu
	fields = ['restaurant','description']

	def form_valid(self, form):
		form.instance.author = self.request.user #the form we're trying to submit is equal to the current logged in user
		return super().form_valid(form)

class MenuDetailView(DetailView):
	model = Menu
