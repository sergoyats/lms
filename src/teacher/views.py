from django.shortcuts import render
from teacher.models import Teacher


def teachers_list(request):
	qs = Teacher.object.all()

	if request.GET.get('fname'):
		qs = qs.filter(first_name=request.GET.get('fname'))

	if request.GET.get('lname'):
		qs = qs.filter(last_name=request.GET.get('lname'))

	if request.GET.get('tel'):
		qs = qs.filter(telephone=request.GET.get('tel'))

	result = '<br>'.join(str(teacher) for teacher in qs)

	return render(request=request,
                  template_name='teachers_list.html',
                  context={'teachers_list': result}
                  )
