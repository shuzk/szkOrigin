from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

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


class StudentsDetailView(GenericAPIView):
    queryset = StudentsInfo.students.all()
    serializer_class = StudentsInfoSerializer

    def get(self, request, pk):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data)


class StudentsListView(ListModelMixin, GenericAPIView):
    queryset = StudentsInfo.students.all()
    serializer_class = StudentsInfoSerializer

    def get(self, request):
        return self.list(request)


# class SDV(RetrieveModelMixin, GenericAPIView):
#     queryset = StudentsInfo.students.all()
#     serializer_class = StudentsInfoSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request)


class StudentsInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = StudentsInfo.students.all()
    serializer_class = StudentsInfoSerializer
    def list(self, request, *args, **kwargs):
        pass
    def retieve(self, request, pk=None):
        pass

    # detail为False，表示不需要处理具体的StudentsInfo对象
    @action(methods=['get'], detail=False)
    def lastest(self, request):
        """返回学生信息"""
        student = StudentsInfo.students.latest('id')
        serializer = self.get_serializer(student)
        return Response(serializer.data)

    # detail为True，表示要处理具体与pk主键对应的StudentsInfo对象
    @action(methods=['put'], detail=True)
    def sname(self, request, pk):
        """查看姓名"""
        student = self.get_object()
        student.sname = request.data.get('sname')
        student.save()
        serializer = self.get_serializer(student)
        return Response(serializer.data)
