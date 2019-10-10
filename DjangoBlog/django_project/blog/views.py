from django.shortcuts import render
from django.http import HttpResponse

posts =[
	{
		'author': 'Fazle',
		'title': 'Django unchained',
		'content': 'Django was developed by the Django software foundation in the year 2005 and designed by Adrian Holovaty and Simon Willison.  The main feature of Django is the High-level python web framework as this framework provides the best way to design the application. As a developer needs to follow the rules or way to implement the project in Django, there is comparatively less freedom compared to the low-level framework but the application created will be neat and clean.',
		'date_created': '10 October 2019'
	},
	{
		'author': 'Tao',
		'title': 'Oracle unchained',
		'content': 'Oracle JDK was developed by Oracle Corporation which was under Sun License and was implemented based on the Java Standard Edition Specification.  It was completely based on Java programming language. Later the license was announced to be released under GPL (General Public License) License. Oracle JDK contains many components as a collection of programming tools in the form of a library.',
		'date_created': '10 October 2019'
	}
]
# Create your views here.
def home(request):
	context ={
		'posts':posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
