# from django.contrib import admin

# Register your models here.


from django.contrib import admin
from test02.models import StudentsInfo, CardsInfo
# from django.apps import AppConfig
#
# class Test02Config(AppConfig):
#     name = 'test02'
#     verbose_name = 'AAAAAAAAAAAAAA'

admin.site.site_header = "学生与卡"
admin.site.site_title = '学生卡aaa'
admin.site.index_title = '欢迎来到学生卡'

# class CardsInfoStackInline(admin.StackedInline):
class CardsInfoTabularInline(admin.TabularInline):
    model = CardsInfo  # 要编辑的对象
    extra = 1  # 附加编辑的数量

# admin.site.register(StudentsInfo)
# admin.site.register(CardsInfo)
@admin.register(StudentsInfo)
class StudentsInfoAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_top = True
    list_display = ['sid', 'old', 'image', 'sname', 'sage', 'sgender']
    list_filter = ['sid', 'sage']
    search_fields = ['sid', 'sname', 'sage', 'sgender']

    # inlines = [CardsInfoStackInline]
    inlines = [CardsInfoTabularInline]
    fieldsets = (
        ('字段分组1', {'fields': ('sid', 'sname', 'image')}),
        ('字段分组2', {
            'fields': ('sage', 'sgender', 'is_delete'),
            'classes': ('collapse')
        }),
    )


@admin.register(CardsInfo)
class CardsInfoAdmin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['cid', 'c_sid', 'pub_date', 'cstudent', 'cname', 'cdate']

    # inlines = [CardsInfoStackInline]
