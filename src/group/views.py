from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from group.forms import GroupAddForm
from group.models import Group


def groups_list(request):
    qs = Group.object.all()
    name = request.GET.get('name')
    specialty = request.GET.get('spec')
    number = request.GET.get('number')

    if name or specialty or number:
        qs = qs.filter(Q(name=name) | Q(spec=specialty) | Q(number=number))

    result = '<br>'.join(str(group) for group in qs)

    return render(request=request,
                  template_name='groups_list.html',
                  context={'groups_list': result}
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
        context={'form': form}
    )
