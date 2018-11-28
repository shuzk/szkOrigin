from django import forms

from test02.models import StudentsInfo


# class StudentForm(forms.Form):
#     id = forms.IntegerField(label='学号', required=True)
#     name = forms.CharField(label='学生姓名', required=True, max_length=20)
    # class Meta:
    #     model = StudentsI

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentsInfo
        fields = ('sid', 'sname')