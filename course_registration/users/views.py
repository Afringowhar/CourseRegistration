from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .decorators import faculty_required, student_required
from courses.models import Course, Registration
from django.contrib.auth import logout

# for registering students and faculty
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'users/login_register.html', {'form': form, 'registering': True})


#for login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'users/login_register.html', {'registering': False})


#redirection to the dashboard based on the role
@login_required
def dashboard(request):
    if request.user.user_type == 'student':
        return redirect('student-dashboard')
    elif request.user.user_type == 'faculty':
        return redirect('faculty-dashboard')
    return redirect('login')


#student dashboard
@student_required
def student_dashboard(request):
    registrations = Registration.objects.filter(student=request.user).select_related('course')
    return render(request, 'users/student_dashboard.html', {
        'registrations': registrations
    })

#faculty dashboard
@faculty_required
def faculty_dashboard(request):
    faculty = request.user.faculty
    courses = Course.objects.filter(faculty=faculty)
    return render(request, 'users/faculty_dashboard.html', {
        'courses': courses
    })

# logout 
def user_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')