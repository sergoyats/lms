from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.db.models import Q

from group.forms import GroupAddForm, GroupEditForm, GroupDeleteForm
from group.models import Group


def groups_list(request):
    qs = Group.object.all()
    name = request.GET.get('name')
    course = request.GET.get('course')
    number = request.GET.get('number')

    if name or course or number:
        qs = qs.filter(Q(name=name) | Q(course=course) | Q(number=number))

    result = '<br>'.join(str(group) for group in qs)

    return render(request=request,
                  template_name='groups_list.html',
                  context={'groups_list': result, 'title': 'Group list'}
                  )


def groups_add(request):
    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupAddForm()

    return render(
        request=request,
        template_name='groups_add.html',
        context={'form': form, 'title': 'Group add'}
    )


def groups_edit(request, id):
    try:
        group = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Group with id={id} doesn't exist")

    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupEditForm(instance=group)

    return render(
        request=request,
        template_name='groups_edit.html',
        context={'form': form, 'title': 'Group edit'}
    )


class GroupsListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups_list.html'
    context_object_name = 'groups_list'
    login_url = reverse_lazy('login')
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('teacher')
        qs = qs.order_by('-id')
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Group list'
        return context


class GroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'groups_edit.html'
    form_class = GroupEditForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'groups_add.html'
    form_class = GroupAddForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups_delete.html'
    form_class = GroupDeleteForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('groups:list')
