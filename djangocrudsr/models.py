from django.db import models

# Create your models here.

class CourseSection(models.Model):
    course_section_id = models.BigAutoField(primary_key=True)
    course_and_section = models.CharField(max_length=55, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
       db_table = 'course_section'

class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    student_id_number = models.CharField(max_length=55, blank=False)
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=False)
    course_and_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)

    class Meta:
        db_table = 'students'

