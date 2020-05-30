from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from student.forms import StudentAddForm, StudentEditForm
from student.models import Student


def generate_students(request):
    n = request.GET.get('N')
    if isinstance(n, int):
        return HttpResponse('<br>'.join([Student.generate_student() for _ in range(n)]))
    else:
        return HttpResponse('Please enter an integer number of students.')


def students_list(request):
    qs = Student.object.all().select_related('group')
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')

    if first_name or last_name or email:
        qs = qs.filter(Q(first_name=first_name) | Q(last_name=last_name) | Q(email=email))
    result = qs

    return render(request=request,
                  template_name='students_list.html',
                  context={'students_list': result, 'title': 'Student list'}
                  )


def students_add(request):
    qs = Student.object.all()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    tel = request.POST.get('tel')
    qs1 = qs.filter(Q(first_name=first_name) & Q(last_name=last_name) & (Q(email=email) | Q(tel=tel)))

    if request.method == 'POST':
        form = StudentAddForm(request.POST)

        if qs1.exists():
            return HttpResponse('This student is already in the database.', status=409)
        else:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('students'))

    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={'form': form, 'title': 'Student add'}
    )


def students_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id={id} doesn't exist")

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentEditForm(instance=student)

    return render(
        request=request,
        template_name='students_edit.html',
        context={'form': form, 'title': 'Student edit'}
    )


def students_delete(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id {id} doesn't exist")

    if request.method == "POST":
        student.delete()
        return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentEditForm(instance=student)

    return render(
        request=request,
        template_name='students_delete.html',
        context={'form': form, 'title': 'Student delete'}
    )


class StudentsListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group')
        qs = qs.order_by('-id')

        if request.GET.get('first_name') or request.GET.get('last_name'):
            qs = qs.filter(Q(first_name=request.GET.get('first_name')) | Q(last_name=request.GET.get('last_name')))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Student list'
        return context


class StudentsUpdateView(UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm

    def get_success_url(self):
        return reverse('students:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit student'
        return context


class StudentsCreateView(CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('students:list')


class StudentsDeleteView(DeleteView):
    model = Student
    template_name = 'students_delete.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('students:list')
