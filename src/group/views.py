from django.shortcuts import render
from django.db.models import Q
from group.models import Group


def groups_list(request):
	qs = Group.object.all()
	name = request.GET.get('name')
	specialty = request.GET.get('spec')
	number = request.GET.get('number')

	qs = qs.filter(Q(name=name) | Q(spec=specialty) | Q(number=number))

	result = '<br>'.join(str(group) for group in qs)

	return render(request=request,
                  template_name='groups_list.html',
                  context={'groups_list': result}
                  )
