from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view(request):
	latest = Auth.objects.all()
	context = {'latest': latest}
	return render(request, 'socialfeed/index.html', context)
