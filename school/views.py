from django.shortcuts import render
from django.http import HttpResponse
from .models import ClassTeacher, Form, Student

def index(request):
    teachers = ClassTeacher.objects.all()
    forms = Form.objects.all()
    student = Student.objects.all()
    return render(request, 'main_page.html', {'teachers': teachers,
                                              'forms': forms})


def teacher(request):
    teachers = ClassTeacher.objects.all()
    forms = Form.objects.all()
    student = Student.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers,
                                            'forms': forms})

def student(request):
    teachers = ClassTeacher.objects.all()
    forms = Form.objects.all()
    student = Student.objects.all()
    return render(request, 'student.html', {'teachers': teachers,
                                            'forms': forms})