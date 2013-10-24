# Create your views here.
from django.http import HttpResponse

from django.contrib.flatpages.models import FlatPage

from django.shortcuts import get_object_or_404

from django.core import serializers


def api(request, url):
    '''
    returns a json response of the requested url if request is a get reqiest
    and their is a FlatPage model instance with the same url.
    '''
    url = "/" + url
    if request.method == 'GET':
        data = FlatPage.objects.filter(url=url)
        output3 = serializers.serialize("json", data, fields=('content'))
        return HttpResponse(output3, mimetype="application/json")
    
    #not sure what to do if not a get request.