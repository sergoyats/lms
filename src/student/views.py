from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student


def generate_students(request, N):
    if isinstance(N, int):
        return HttpResponse('\n'.join([Student.generate_student() for _ in range(N)]))
    else:
        return HttpResponse('Please enter an integer number of students.')
