from django.db import models

# Create your models here.


class StudentsInfoManager(models.Manager):
    def all(self):
        return super().filter(is_delete=False)
    def create_student(self, id, name, age):
        student = self.model()
        student.sid = id
        student.sname = name
        student.sage = age
        student.sgender = 0
        student.is_delete = False
        # student.image = True
        student.save()
        return student

class StudentsInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    sid = models.IntegerField(primary_key=True, verbose_name='学号')
    sname = models.CharField(max_length=20, verbose_name='姓名', unique=True)
    sage = models.IntegerField(verbose_name='年龄')
    sgender = models.BooleanField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    # You are trying to add a non-nullable field 'sdate' to studentsinfo without a default; we can't do that (the database needs something to populate existing rows).
    # sdate = models.DateField(verbose_name='入学日期')
    # scomment = models.CharField
    is_delete = models.BooleanField(default=False, verbose_name='删除个人')
    image = models.ImageField(upload_to='test02', verbose_name='图片', null=True)

    def old(self):
        return self.sage-20
    old.short_description = '二十几岁'
    old.admin_order_field = 'sage'

    class Meta:
        db_table = 'students'  # 指明数据库表名
        verbose_name = '学生表'  # 在admin站点中显示的名称
        verbose_name_plural =verbose_name  # 显示的复数名称

    # 在admin站点中显示字段
    def __str__(self):
        return self.sname

    students = StudentsInfoManager()

class CardsInfoManager(models.Manager):
    def all(self):
        return super().filter(is_delete=False)
    def create_card(self, id, name, date, student):
        card = self.model()
        card.cid = id
        card.cname = name
        card.cdate = date
        card.cstudent = student
        card.is_delete = False
        card.save()
        return card


class CardsInfo(models.Model):
    cid = models.IntegerField(primary_key=True, verbose_name='卡号')
    cname = models.CharField(max_length=20, verbose_name='什么卡', unique=True)
    cdate = models.DateField(verbose_name='注册卡日期')
    cstudent = models.ForeignKey(StudentsInfo, on_delete=models.CASCADE, verbose_name='卡外键')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    def pub_date(self):
        return self.cdate.strftime('%Y年%m月%d日')
    pub_date.short_description = '办理日期'

    def c_sid(self):
        return self.cstudent.sid
    c_sid.short_description = '所属学生id'
    c_sid.admin_order_field = 'cid'

    class Meta:
        db_table = 'cards'
        # 以下两行在admin中显示名称
        verbose_name = '卡名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cname

    cards = CardsInfoManager()

