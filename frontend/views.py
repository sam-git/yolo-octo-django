# Create your views here.
from django.http import HttpResponse

def call_api(request, url):
    return HttpResponse("Calling API")