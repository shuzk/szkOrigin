import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from .models import StudentsInfo, CardsInfo
from rest_framework.views import APIView
from .serializers import StudentsInfoSerializer


# GET /books/
class StudentsListAPIView(APIView):
    def get(self, request):
        # 数据库查询
        # queryset = StudentsInfo.objects.all()
        queryset = StudentsInfo.students.all()
        # 构建序列化器对象进行序列化操作
        serializer = StudentsInfoSerializer(queryset, many=True)

        return Response(serializer.data)
# 上一个是APIView