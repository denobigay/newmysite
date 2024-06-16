from django.shortcuts import render

# Create your views here.

def index_course_section(request):
    return render(request, 'course_section/index.html')