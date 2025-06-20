from django.db import models
from users.models import Faculty, User
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='courses')
    credits = models.PositiveIntegerField(default=3)

    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Registration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')
    registration_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f"{self.student} registered for {self.course}"