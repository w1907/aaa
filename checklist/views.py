from django.shortcuts import render
from django.http import HttpResponse

def checkList(request):
	data = {}
	template_name = "checklist.html"
	return render(request, template_name, data)