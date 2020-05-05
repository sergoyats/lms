from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student


def generate_students(request):
	n = request.GET.get('N')
    if isinstance(n, int):
        return HttpResponse('\n'.join([Student.generate_student() for _ in range(n)]))
    else:
        return HttpResponse('Please enter an integer number of students.')


def students_list(request):
	qs = Student.object.all()
	
	if request.GET.get('fname'):
		qs = qs.filter(first_name=request.GET.get('fname'))
	
	if request.GET.get('lname'):
		qs = qs.filter(last_name=request.GET.get('lname'))
		
	if request.GET.get('email'):
		qs = qs.filter(email=request.GET.get('email'))

	result = '<br>'.join(str(student) for student in qs)
	
	return render(request=request,
                  template_name='students_list.html',
                  context={'students_list': result}
                  )
