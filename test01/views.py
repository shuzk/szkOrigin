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

# =========== 类视图 ===============
# HTTP请求方式的支持时，便需要在一个函数中编写不同的业务逻辑，代码可读性与复用性都不佳-------------------------
def register(request):
    """处理注册"""

    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':
        # 处理GET请求，返回注册页面
        return render(request, 'register.html')
    else:
        # 处理POST请求，实现注册逻辑
        return HttpResponse('这里实现注册逻辑')

# 使用类视图可以将视图对应的不同请求方式以类中的不同方法来区别定义------------------
from django.views.generic import View

class RegisterView(View):
    """类视图：处理注册"""

    def get(self, request):
        """处理GET请求，返回注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """处理POST请求，实现注册逻辑"""
        return HttpResponse('这里实现注册逻辑')


# 给类视图添加装饰其----------------------------
# 此种方式会为类视图中的所有请求方法都加上装饰器行为（因为是在视图入口处，分发请求方式前）
def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器my_decorator被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper

class DemoView(View):
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    def post(self, request):
        print('post方法')
        return HttpResponse('ok')

def my_decorator2(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器my_decorator2被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)

    return wrapper
# ====================================================
# 类视图Mixin扩展类
class BaseView(View):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view

class Base2View(View):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator2(view)
        return view

class DemoView2(BaseView, Base2View):
    def get(self, request):
        return HttpResponse('get page')
    def post(self, request):
        return HttpResponse('post page')
#-------------------------------------------------------
class BaseViewA(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        print(super)
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view

class Base2ViewA(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        print(super)
        view = super().as_view(*args, **kwargs)
        view = my_decorator2(view)
        return view

class DemoView3(BaseViewA, Base2ViewA, View):
    def get(self, request):
        return HttpResponse('get page')
    def post(self, request):
        return HttpResponse('post page')