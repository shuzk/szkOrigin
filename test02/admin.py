# from django.contrib import admin

# Register your models here.


from django.contrib import admin
from test02.models import StudentsInfo, CardsInfo

# admin.site.register(StudentsInfo)
# admin.site.register(CardsInfo)
@admin.register(StudentsInfo)
class StudentsInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(CardsInfo)
class CardsInfoAdmin(admin.ModelAdmin):
    pass