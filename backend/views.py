# Create your views here.
from django.http import HttpResponse

from django.contrib.flatpages.models import FlatPage

from django.shortcuts import get_object_or_404

from django.core import serializers


def api(request, url):
    # # email = request.session['email']
    # context_dict = {'email':email}
    # if university:
    #     context_dict['university'] = university
    # if not email is None:
    #     return render(request, 'omicron/unsupported_email_fb.html', context_dict)
    # else:
    #     #LOG ERROR

    if request.method == 'GET':
	    url = "/" + url

	    output = FlatPage.objects.all()
	    output2 = "Returning json of " + url
	    # output3 = FlatPage.objects.get(url=url)
	    # output3 = get_object_or_404(FlatPage, url=url)
	    # return HttpResponse(output3)


	    # try: 
	    #     output3 = FlatPage.objects.get(url=url)
	    #     return HttpResponse(output3)
	    # except FlatPage.DoesNotExist:
	    #     return HttpResponse("Does not exist: " + url)

	    try: 
	        data = FlatPage.objects.filter(url=url)
	        output3 = serializers.serialize("json", data, fields=('content'))
	        return HttpResponse(output3)
	    except FlatPage.DoesNotExist:
	        return HttpResponse("Does not exist: " + url)
    