from django.urls import path
from .views import (course_list, course_detail, create_course, update_course, 
                   delete_course, register_courses, unregister_course, my_courses)

urlpatterns = [
    path('course/', course_list, name='course-list'),
    path('<int:pk>/', course_detail, name='course-detail'),
    path('create/', create_course, name='create-course'),
    path('<int:pk>/update/', update_course, name='update-course'),
    path('<int:pk>/delete/', delete_course, name='delete-course'),
    path('registercourse/', register_courses, name='register-courses'),
    path('unregister/<int:pk>/', unregister_course, name='unregister-course'),
    path('my-courses/', my_courses, name='my-courses'),
]