from django.urls import path
from . import views

urlpatterns = [
    path('course', views.index_course_section),
    
]