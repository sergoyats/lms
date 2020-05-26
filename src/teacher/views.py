from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from teacher.forms import TeacherAddForm, TeacherEditForm, TeacherDeleteForm
from teacher.models import Teacher


def generate_teachers(request):
    n = request.GET.get('N')
    if isinstance(n, int):
        return HttpResponse('<br>'.join([Teacher.generate_teacher() for _ in range(n)]))
    else:
        return HttpResponse('Please enter an integer number of teachers.')


def teachers_list(request):
    qs = Teacher.object.all()
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    tel = request.GET.get('tel')

    if first_name or last_name or tel:
        qs = qs.filter(Q(first_name=first_name) | Q(last_name=last_name) | Q(tel=tel))
    result = qs

    return render(request=request,
                  template_name='teachers_list.html',
                  context={'teachers_list': result, 'title': 'Teacher list'}
                  )


def teachers_add(request):
    qs = Teacher.object.all()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get("email")
    tel = request.POST.get("tel")
    qs1 = qs.filter(Q(first_name=first_name) & Q(last_name=last_name) & (Q(email=email) | Q(tel=tel)))

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


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers_list.html'
    context_object_name = 'teachers_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Teacher list'
        return context


class TeachersUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers_edit.html'
    form_class = TeacherEditForm

    def get_success_url(self):
        return reverse('teachers:list')


class TeachersCreateView(CreateView):
    model = Teacher
    template_name = 'teachers_add.html'
    form_class = TeacherAddForm

    def get_success_url(self):
        return reverse('teachers:list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers_delete.html'
    form_class = TeacherDeleteForm

    def get_success_url(self):
        return reverse('teachers:list')
