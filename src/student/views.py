from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student


def generate_students(request, N):
	n = request.GET.get('N')
    if isinstance(n, int):
        return HttpResponse('\n'.join([Student.generate_student() for _ in range(n)]))
    else:
        return HttpResponse('Please enter an integer number of students.')
