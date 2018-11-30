from rest_framework import serializers

from test02.models import StudentsInfo


class StudentsInfoSerializer(serializers.ModelSerializer):
    """学生表数据序列器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    sid = serializers.IntegerField(label='ID', read_only=True)
    sname = serializers.CharField(label='名字', max_length=20)
    sage = serializers.IntegerField(label='年龄', required=False)
    # sgender = serializers.BooleanField(label='性别', required=False)
    sgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    is_delete = serializers.BooleanField(label='逻辑删除', required=False)
    image = serializers.ImageField(label='图片', required=False)

    class Meta:
        model = StudentsInfo
        fields = '__all__'


class CardsInfoSerializer(serializers.Serializer):
    """卡数据序列化器"""
    cid = serializers.IntegerField(label='卡id', read_only=True)
    cname = serializers.CharField(label='卡名称', max_length=20)
    cdate = serializers.DateField(label='办卡日期', required=False)
    # 外键序列化方式1——PrimaryKeyRelatedField
    # cstudent = serializers.PrimaryKeyRelatedField(label='关联学生', queryset=StudentsInfo.students.all())
    # 外键序列化方式2——StringRelatedField
    # cstudent = serializers.StringRelatedField(label='关联学生')
    # 外键序列化方式3——HyperlinkedRelatedField
    # cstudent = serializers.HyperlinkedRelatedField(label='关联学生', read_only=True, view_name='students')
    # SlugRelatedField
    # cstudent = serializers.SlugRelatedField(label='关联学生', read_only=True, slug_field='sname')
    # 使用关联对象的序列化器
    # cstudent = StudentsInfoSerializer()
    # 重写to_representation方法，适用于所有的字段
    class cStudentRelatedField(serializers.RelatedField):
        """自定义用于处理外键学生的字段"""
        def to_representation(self, value):
            return 'cStudent: %d  %s'%(value.sid, value.sname)
    cstudent = cStudentRelatedField(read_only=True)


    is_delete = serializers.BooleanField(label='逻辑删除卡', required=False)
