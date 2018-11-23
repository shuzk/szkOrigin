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


def weather2(request, year, city):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('OK')


# /qs/?a=1&b=2&a=3
def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)  # 3
    print(b)  # 2
    print(alist)  # ['1', '3']
    return HttpResponse('OK')


def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')


import json


def get_body_json(request):
    json_str = request.body
    json_str = json_str.decode()  # python3.6 无需执行此步
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('OK')


def get_headers(request):
    print(request.META['CONTENT_TYPE'])
    return HttpResponse('OK')


from django.http import HttpResponse


def demo_view(request):
    return HttpResponse('itcast python', status=400)
    # 或者
    # response = HttpResponse('itcast python')
    # response.status_code = 400
    # response['Itcast'] = 'Python'
    # return response


from django.http import JsonResponse


def demo_view2(request):
    return JsonResponse({'city': 'beijing', 'subject': 'python'})


from django.shortcuts import redirect


def demo_view3(request):
    return redirect('/static/index.html')


def cookie_set(request):
    response = HttpResponse('ok')
    response.set_cookie('itcast1', 'python1')  # 临时cookie
    response.set_cookie('itcast2', 'python2', max_age=3600)  # 有效期一小时
    return response
def cookie_read(request):
    cookie1 = request.COOKIES.get('itcast1')
    print(cookie1)
    return HttpResponse('OK')