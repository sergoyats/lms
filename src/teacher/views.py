from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from teacher.forms import TeacherAddForm
from teacher.models import Teacher


def generate_teachers(request):
    n = request.GET.get('N')
    if isinstance(n, int):
        return HttpResponse('<br>'.join([Teacher.generate_teacher() for _ in range(n)]))
    else:
        return HttpResponse('Please enter an integer number of teachers.')


def teachers_list(request):
    qs = Teacher.object.all()
    first_name = request.GET.get('fname')
    last_name = request.GET.get('lname')
    telephone = request.GET.get('tel')

    if first_name or last_name or telephone:
        qs = qs.filter(Q(fname=first_name) | Q(lname=last_name) | Q(tel=telephone))

    result = '<br>'.join(str(teacher) for teacher in qs)

    return render(request=request,
                  template_name='teachers_list.html',
                  context={'teachers_list': result}
                  )


def teachers_add(request):
    qs = Teacher.object.all()
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get("email")
    telephone = request.POST.get("tel")
    qs1 = qs.filter(Q(fname=first_name) & Q(lname=last_name) & (Q(email=email) | Q(tel=telephone)))

    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid() and (qs1 in qs):
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
        else:
            return HttpResponse('This teacher is already in the database.')
    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name='teachers_add.html',
        context={'form': form}
    )
