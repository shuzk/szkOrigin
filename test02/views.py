import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from .models import StudentsInfo, CardsInfo
from rest_framework.views import APIView
from .serializers import StudentsInfoSerializer
from rest_framework.generics import GenericAPIView


# GET /books/
# class StudentsListAPIView(APIView):
#     def get(self, request):
#         # 数据库查询
#         # queryset = StudentsInfo.objects.all()
#         queryset = StudentsInfo.students.all()
#         # 构建序列化器对象进行序列化操作
#         serializer = StudentsInfoSerializer(queryset, many=True)
#
#         return Response(serializer.data)


# GET /books/
class StudentsListAPIView(GenericAPIView):
    queryset = StudentsInfo.students.all()
    serializer_class = StudentsInfoSerializer

    def get(self, request):
        # 数据库查询
        # queryset = StudentsInfo.objects.all()
        # queryset = StudentsInfo.students.all()
        qs = self.get_queryset()
        # 构建序列化器对象进行序列化操作
        # serializer = StudentsInfoSerializer(queryset, many=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


# GET  /students/<>/
class StudentsDetailAPIView(GenericAPIView):
    queryset = StudentsInfo.students.all()
    serializer_class = StudentsInfoSerializer

    def get(self, request, pk):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data)