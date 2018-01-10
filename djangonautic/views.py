from django.http import HttpResponse
from django.shortcuts import render

#Function that will fire off when user visits homepage
def homepage(request):
	# return HttpResponse("HOME")
	return render(request, 'homepage.html')

#Function for when user visits /about url
def about(request):
	# return HttpResponse(slug)
	return render(request, 'about.html')

