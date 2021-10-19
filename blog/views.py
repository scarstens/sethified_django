from django.shortcuts import render

posts = [
	{
		'author'     : 'Seth Carstens',
		'title'      : 'My First Django Post',
		'content'    : 'Getting started with Python Django framework.',
		'date_posted': 'October 18, 2021'
	},
	{
		'author'     : 'Seth Carstens',
		'title'      : 'Using render to pull static html files',
		'content'    : 'Replacing HttpResponse with render functions to use SSI to include static HTML.',
		'date_posted': 'October 18, 2021'
	},
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', { 'title': 'About Seth Carstens' })
