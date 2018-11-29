from rest_framework import serializers

from test02.models import StudentsInfo


class StudentsInfoSerializer(serializers.ModelSerializer):
    """学生表数据序列器"""

    class Meta:
        model = StudentsInfo
        fields = '__all__'
