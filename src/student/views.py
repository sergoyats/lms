from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from student.forms import StudentAddForm
from student.models import Student


def generate_students(request):
    n = request.GET.get('N')
    if isinstance(n, int):
        return HttpResponse('<br>'.join([Student.generate_student() for _ in range(n)]))
    else:
        return HttpResponse('Please enter an integer number of students.')


def students_list(request):
    qs = Student.object.all()
    first_name = request.GET.get('fname')
    last_name = request.GET.get('lname')
    email = request.GET.get("email")

    if first_name or last_name or email:
        qs = qs.filter(Q(fname=first_name) | Q(lname=last_name) | Q(email=email))

    result = '<br>'.join(str(student) for student in qs)

    return render(request=request,
                  template_name='students_list.html',
                  context={'students_list': result}
                  )


def students_add(request):
    qs = Student.object.all()
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get("email")
    telephone = request.POST.get("tel")
    qs1 = qs.filter(Q(fname=first_name) & Q(lname=last_name) & (Q(email=email) | Q(tel=telephone)))

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
		
		if qs1 in qs:
			return HttpResponse(409, 'Conflict: This student is already in the database.')
        else:
			if form.is_valid:
				form.save()
				return HttpResponseRedirect(reverse('students'))
            
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={'form': form}
    )
