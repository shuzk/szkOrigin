from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    a = reverse('test01:index')
    return HttpResponse('hello %s ' % a)


def weather(request, city, year):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('OK')
