from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_id = models.CharField(max_length=20, unique=True)
  
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.student_id})"

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    faculty_id = models.CharField(max_length=20, unique=True)

    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.faculty_id})"