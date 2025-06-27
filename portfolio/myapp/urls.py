from django.urls import path
from . import views

urlpatterns = [
    path('homepage/<int:id>', views.homepage),
    path('aboutus', views.aboutUs),
    path('studentform', views.student_form, name = 'student_form')
]