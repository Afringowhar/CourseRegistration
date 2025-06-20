from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Registration
from .forms import CourseForm, RegistrationForm
from users.decorators import faculty_required, student_required
from django.utils import timezone

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    is_registered = False
    if request.user.user_type == 'student':
        is_registered = Registration.objects.filter(student=request.user, course=course).exists()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_registered': is_registered
    })

@faculty_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.faculty = request.user.faculty
            course.save()
            messages.success(request, 'Course created successfully!')
            return redirect('faculty-dashboard')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

@faculty_required
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk, faculty=request.user.faculty)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('faculty-dashboard')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})

@faculty_required
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk, faculty=request.user.faculty)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully!')
        return redirect('faculty-dashboard')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})

@student_required
def register_courses(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, student=request.user)
        if form.is_valid():
            selected_courses = form.cleaned_data['courses']
            
            # Check if registering would exceed the 2-course limit
            current_registrations = Registration.objects.filter(student=request.user).count()
            if current_registrations + len(selected_courses) > 2:
                messages.error(request, 'You can register for a maximum of 2 courses.')
                return redirect('register-courses')
            
            for course in selected_courses:
                Registration.objects.create(
                    student=request.user,
                    course=course,
                    registration_date=timezone.now()
                )
            messages.success(request, 'Registration successful!')
            return redirect('student-dashboard')
    else:
        form = RegistrationForm(student=request.user)
    return render(request, 'courses/registration_form.html', {'form': form})

@student_required
def unregister_course(request, pk):
    registration = get_object_or_404(Registration, pk=pk, student=request.user)
    if request.method == 'POST':
        registration.delete()
        messages.success(request, 'Successfully unregistered from the course.')
        return redirect('student-dashboard')
    return render(request, 'courses/unregister_confirm.html', {'registration': registration})

@student_required
def my_courses(request):
    registrations = Registration.objects.filter(student=request.user).select_related('course')
    return render(request, 'courses/my_courses.html', {'registrations': registrations})