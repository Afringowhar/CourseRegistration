from django import forms
from .models import Course, Registration

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'credits']
 

class RegistrationForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)
        
        if self.student:
            registered_courses = self.student.registrations.values_list('course_id', flat=True)
            self.fields['courses'].queryset = Course.objects.exclude(id__in=registered_courses)