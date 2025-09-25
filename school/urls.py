from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.teacher, name='teacher'),
    path('form/', views.student, name='form'),
    path('<int:form_id>', views.single_form, name='single_form')   
]
