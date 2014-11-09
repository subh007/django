from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def volunteerview(request):
    #return HttpResponse('volunteer')
    return render_to_response('volun/base.html',{'author' : 'subh'})