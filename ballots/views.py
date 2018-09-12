from django.shortcuts import render
from django.http  import  HttpResponse
# Create your views here.

def index(request):
	return HttpResponse('<html><body><h1><strong>Ballots Index.</strong></h1></body></html>')
