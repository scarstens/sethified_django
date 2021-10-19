from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all().order_by('-date_posted')[:10]
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', { 'title': 'About Seth Carstens' })
