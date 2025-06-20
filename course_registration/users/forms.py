from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Faculty

class UserRegisterForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
    student_id = forms.CharField(max_length=20, required=False)
    faculty_id = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'user_type']

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        
        if user_type == 'student':
            if not cleaned_data.get('student_id'):
                raise forms.ValidationError("Student ID is required for students.")
        elif user_type == 'faculty':
            if not cleaned_data.get('faculty_id'):
                raise forms.ValidationError("Faculty ID is required for faculty.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data['user_type']
        user.user_type = user_type
        
        if commit:
            user.save()
            
            if user_type == 'student':
                Student.objects.create(
                    user=user,
                    student_id=self.cleaned_data['student_id'],
                    
                )
            elif user_type == 'faculty':
                Faculty.objects.create(
                    user=user,
                    faculty_id=self.cleaned_data['faculty_id'],
                )
        
        return user