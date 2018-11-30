from rest_framework import serializers

from test02.models import StudentsInfo


class StudentsInfoSerializer(serializers.ModelSerializer):
    """学生表数据序列器"""
    sid = serializers.IntegerField(label='ID', read_only=True)
    sname = serializers.CharField(label='名字', max_length=20)
    sage = serializers.IntegerField(label='年龄', required=False)
    sgender = serializers.BooleanField(label='性别', required=False)
    is_delete = serializers.BooleanField(label='逻辑删除', required=False)
    image = serializers.ImageField(label='图片', required=False)
    class Meta:
        model = StudentsInfo
        fields = '__all__'
