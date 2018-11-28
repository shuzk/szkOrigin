# from django.shortcuts import render
# from django.views.generic import View
# from django.http import HttpResponse
#
# from .forms import StudentForm
#
#
# class StudentView(View):
#     def get(self, request):
#         form = StudentForm()
#         return render(request, 'student.html', {'form': form})
#
#     def post(self, request):
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return HttpResponse('OK')
#         else:
#             return render(request, 'student.html', {'form': form})

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    # 1.获取模板
    tem = loader.get_template('index.html')
    # 2.渲染模板
    content = {'city': '北京'}
    return HttpResponse(tem.render(content))
    return render(request, 'index.html', context)


def index2(request):
    context = {
        'city': '北京',
        'adict': {
            'name': '西游记',
            'author': '吴承恩'
        },
        'alist': [1, 2, 3, 4, 5]
    }
    return render(request, 'index.html', context)
