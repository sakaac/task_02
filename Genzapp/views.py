from django.shortcuts import render


def Genzapp(request):
	context = {
	'msg': 'Hello World!'
	}
	return render(request, "task02.html", context)
# Create your views here.
