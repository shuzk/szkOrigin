from django.db import models

# Create your models here.
class StudentsInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    sid = models.IntegerField(primary_key=True, verbose_name='学号')
    sname = models.CharField(max_length=20, verbose_name='姓名', unique=True)
    sage = models.IntegerField(verbose_name='年龄')
    sgender = models.BooleanField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    is_delete = models.BooleanField(default=False, verbose_name='删除个人')

    class Meta:
        db_table = 'students'  # 指明数据库表名
        verbose_name = '学生表'  # 在admin站点中显示的名称
        verbose_name_plural =verbose_name  # 显示的复数名称

