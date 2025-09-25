from django.db import models
from django.utils import timezone



class ClassTeacher(models.Model):
    subjects = models.JSONField(default=list)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"


class Form(models.Model):
    classteacher = models.ForeignKey(ClassTeacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4)
    created_at = models.DateTimeField(default=timezone.now)
    @property
    def students_qty(self):
        return self.student_set.count()

    def __str__(self):
        return self.title
    

class Student(models.Model):
    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING)  # , on_delete=models.CASCADE
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, default="")
    age = models.IntegerField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"