from django.urls import path
from .views import student_dashboard, faculty_dashboard, dashboard, user_login, user_logout

urlpatterns = [
    path('student/dashboard/', student_dashboard, name='student-dashboard'),
    path('faculty/dashboard/', faculty_dashboard, name='faculty-dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
]