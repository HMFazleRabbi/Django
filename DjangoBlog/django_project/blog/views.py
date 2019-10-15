from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)

# Create your views here.
def home(request):
	context ={
		'posts':Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	"""docstring for PostListView"""
	model=Post
	template_name='blog/home.html' #app/model_List.gtml
	context_object_name='posts'
	ordering=['-datecreated'] #- ve sign for reverse order
	paginate_by=5

class UserPostListView(ListView):
	"""docstring for PostListView"""
	model=Post
	template_name='blog/user_posts.html' #app/model_List.gtml
	context_object_name='posts'
	paginate_by=5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-datecreated')

class PostDetailView(DetailView):
	"""docstring for PostListView"""
	model=Post

class PostCreateView(LoginRequiredMixin, CreateView):
	"""docstring for PostListView"""
	model=Post
	fields=['title', 'content']

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	"""docstring for PostListView"""
	model=Post
	fields=['title', 'content']

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	"""docstring for PostListView"""
	model=Post
	success_url='/'


	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'Django Blog About'})
