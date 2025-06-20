from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def student_required(view_func):
    def test_func(user):
        return user.is_authenticated and user.user_type == 'student'
    decorated_view_func = user_passes_test(test_func, login_url='login')
    return decorated_view_func(view_func)

def faculty_required(view_func):
    def test_func(user):
        return user.is_authenticated and user.user_type == 'faculty'
    decorated_view_func = user_passes_test(test_func, login_url='login')
    return decorated_view_func(view_func)