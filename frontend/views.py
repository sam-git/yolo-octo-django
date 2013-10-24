# Create your views here.
from django.http import HttpResponse

from backend.views import api

def call_api(request, url):
    return api(request, url)