from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def volunteerview(request):
    return HttpResponse('volunteer')