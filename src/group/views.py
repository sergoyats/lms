from django.shortcuts import render
from group.models import Group

def groups_list(request):
    qs = Group.object.all()
    Name = request.GET.get('name')
    Specialty = request.GET.get('spec')
    Number = request.GET.get('number')

    if Name or Specialty or Number:
        qs = qs.filter((name=Name) | (spec=Specialty) | (number=Number))

    result = '<br>'.join(str(group) for group in qs)

    return render(request=request,
                  template_name='groups_list.html',
                  context={'groups_list': result}
                  )
