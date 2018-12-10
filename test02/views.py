import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from .models import StudentsInfo, CardsInfo
from rest_framework.views import APIView
from .serializers import StudentsInfoSerializer
from rest_framework.generics import GenericAPIView
#
#
# # GET /books/
# # class StudentsListAPIView(APIView):
# #     def get(self, request):
# #         # 数据库查询
# #         # queryset = StudentsInfo.objects.all()
# #         queryset = StudentsInfo.students.all()
# #         # 构建序列化器对象进行序列化操作
# #         serializer = StudentsInfoSerializer(queryset, many=True)
# #
# #         return Response(serializer.data)
#
#
# # GET /books/
# # class StudentsListAPIView(GenericAPIView):
# #     queryset = StudentsInfo.students.all()
# #     serializer_class = StudentsInfoSerializer
# #
# #     def get(self, request):
# #         # 数据库查询
# #         # queryset = StudentsInfo.objects.all()
# #         # queryset = StudentsInfo.students.all()
# #         qs = self.get_queryset()
# #         # 构建序列化器对象进行序列化操作
# #         # serializer = StudentsInfoSerializer(queryset, many=True)
# #         serializer = self.get_serializer(qs, many=True)
# #         return Response(serializer.data)
#
# from rest_framework import mixins
# # GET /books/
# # class StudentsListAPIView(mixins.ListModelMixin, GenericAPIView):
# #     queryset = StudentsInfo.students.all()
# #     serializer_class = StudentsInfoSerializer
# #
# #     def get(self, request):
# #         return self.list(request)
# from rest_framework.generics import ListAPIView
# # GET /books/
# class StudentsListAPIView(ListAPIView):
#     queryset = StudentsInfo.students.all()
#     serializer_class = StudentsInfoSerializer
#
#
# # GET  /students/<>/
# class StudentsDetailAPIView(GenericAPIView):
#     queryset = StudentsInfo.students.all()
#     serializer_class = StudentsInfoSerializer
#
#     def get(self, request, pk):
#         student = self.get_object()
#         serializer = self.get_serializer(student)
#         return Response(serializer.data)



# 视图集
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from test02.models import StudentsInfo
from rest_framework.decorators import action


class StudentsInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = StudentsInfo.students.all()
    serializer_class = StudentsInfoSerializer

    @action(methods=['get'], detail=False)
    def latest(self, request):
        """返回最新的学生信息"""
        student = StudentsInfo.students.latest('sid')
        serializer = self.get_serializer(student)
        return Response(serializer.data)

    # detail为True时，表示要处理具体与pk主键对应的对象
    @action(methods=['put'], detail=True)
    def age(self, request, pk):
        student = self.get_object()
        student.sage = request.data.get('age')
        student.save()
        serializer = self.get_serializer(student)
        return Response(serializer.data)
    # def list(self):
    #     pass
    #
    # def retrieve(self):
    #     pass












