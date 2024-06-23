from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.index_course_section, name='index'),
    path('add_course/', views.create_course, name='create_course'),
    path('course_section_store/', views.store_course, name='store_course'),
    path('course/view/<int:course_section_id>/', views.view_course_section, name='view_course_section'),
    path('course/edit/<int:course_section_id>/', views.edit_course_section, name='edit_course_section'),
    path('course/delete/<int:course_section_id>/', views.delete_course_section, name='delete_course_section'),

    path('students/', views.student_index, name='student_index'),
    path('add_student/', views.create_student, name='create_student'),
    path('students/store/', views.store_student, name='store_student'),
    path('students/view/<int:student_id>/', views.view_students, name='view_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),


]
