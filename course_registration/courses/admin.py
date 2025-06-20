from django.contrib import admin
from .models import Course, Registration

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'faculty')
    list_filter = ('faculty',)
    search_fields = ('name', 'code', 'faculty__user__first_name', 'faculty__user__last_name')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'registration_date')
    list_filter = ('course', 'registration_date')
    search_fields = ('student__username', 'course__name')

admin.site.register(Course, CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)