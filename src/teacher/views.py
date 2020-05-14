from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from teacher.forms import TeacherAddForm, TeacherEditForm
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
                  context={'teachers_list': result, 'title': 'Teacher list'}
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

        if qs1.exists():
            return HttpResponse('This teacher is already in the database.', status=409)
        else:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('teachers'))

    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name='teachers_add.html',
        context={'form': form, 'title': 'Teacher add'}
    )


def teachers_edit(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Teacher with id {id} doesn't exist")

    if request.method == "POST":
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherEditForm(instance=teacher)

    return render(
        request=request,
        template_name='teachers_edit.html',
        context={'form': form, 'title': 'Teacher edit'}
    )
