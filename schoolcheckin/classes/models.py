from django.db import models
from management.models import ClassRoom, Student
# Create your models here.
class StudentAttendance(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attend = models.BooleanField()
    timestamp = models.DateTimeField(auto_now=True)