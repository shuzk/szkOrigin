from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .forms import StudentForm
from .serializers import StudentsInfoSerializer
from .models import StudentsInfo


class StudentView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'student.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():  # 验证表单数据
            print(form.cleaned_data)  # 获取验证后的表单数据
            return HttpResponse('OK')
        else:
            return render(request, 'student.html', {'form': form})


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

class StudentsInfoViewSet(ModelViewSet):
    # queryset = StudentsInfo.objects.all()  # StudentsInfo没有默认属性objects，自定义属性students
    queryset = StudentsInfo.students.all()
    print(queryset)
    serializer_class = StudentsInfoSerializer

class StudentsListView(APIView):
    def get(self,request):
        students = StudentsInfo.students.all()
        serializer = StudentsInfoSerializer(students, many=True)
        return Response(serializer.data)