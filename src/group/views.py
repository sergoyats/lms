from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from group.forms import GroupAddForm, GroupEditForm
from group.models import Group


def groups_list(request):
    qs = Group.object.all()
    name = request.GET.get('name')
    course = request.GET.get('course')
    number = request.GET.get('number')

    if name or specialty or number:
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
