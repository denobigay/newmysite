from django.shortcuts import render, redirect, get_object_or_404
from .models import CourseSection, Student
from django.contrib import messages

# CourseSection Views

def index_course_section(request):
    courses = CourseSection.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course_section/index.html', context)

def create_course(request):
    return render(request, 'course_section/add_course.html')

def store_course(request):
    course_and_section = request.POST.get('course_section')
    CourseSection.objects.create(course_and_section=course_and_section)
    messages.success(request, 'You have added new course and section!')
    return redirect('/courses')

def view_course_section(request, course_section_id):
    course_section = get_object_or_404(CourseSection, pk=course_section_id)
    context = {
        'course_section': course_section,
    }
    return render(request, 'course_section/view_course.html', context)

def edit_course_section(request, course_section_id):
    course_section = get_object_or_404(CourseSection, pk=course_section_id)
    if request.method == 'POST':
        course_and_section = request.POST.get('course_and_section')
        course_section.course_and_section = course_and_section
        course_section.save()
        messages.success(request, 'Course and section updated successfully!')
        return redirect('/courses')
    context = {
        'course_section': course_section,
    }
    return render(request, 'course_section/edit_course.html', context)

def delete_course_section(request, course_section_id):
    course_section = get_object_or_404(CourseSection, pk=course_section_id)
    course_section.delete()
    messages.error(request, 'Course and section deleted successfully!')
    return redirect('/courses')

# Student Views

def student_index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/index.html', context)

def create_student(request):
    courses = CourseSection.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'students/add_student.html', context)

def store_student(request):
    if request.method == 'POST':
        student_id_number = request.POST.get('student_id_number')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        course_and_section_id = request.POST.get('course_and_section')
        
        course_and_section = get_object_or_404(CourseSection, pk=course_and_section_id)
        
        Student.objects.create(
            student_id_number=student_id_number,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            course_and_section=course_and_section
        )
        
        messages.success(request, 'Student added successfully!')
        return redirect('/students')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('/students')

def view_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/view_student.html', context)

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = CourseSection.objects.all()
    context = {
        'student': student,
        'courses': courses
    }
    return render(request, 'students/edit_student.html', context)

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student_id_number = request.POST.get('student_id_number')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        course_and_section_id = request.POST.get('course_and_section')
        
        course_and_section = get_object_or_404(CourseSection, pk=course_and_section_id)
        
        student.student_id_number = student_id_number
        student.first_name = first_name
        student.middle_name = middle_name
        student.last_name = last_name
        student.course_and_section = course_and_section
        
        student.save()  # Save the updated student object

        messages.success(request, 'Student updated successfully!')
        return redirect('student_index')  # Redirect to the student index page
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('edit_student', student_id=student_id)

def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, student_id=student_id)
        student.delete()
        messages.success(request, 'Student deleted successfully.')
    return redirect('student_list')