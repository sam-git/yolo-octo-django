# Create your views here.
from django.http import HttpResponse

from backend.views import api

def call_api(request, identifier):
	'''
	uses the url as an identifier to make a call to the api in the backend app.
	'''
    return api(request, identifier)