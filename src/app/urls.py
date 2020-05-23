"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from student.views import students_list, generate_students, students_add, students_edit, students_delete
from teacher.views import teachers_list, generate_teachers, teachers_add, teachers_edit
from group.views import groups_list, groups_add, groups_edit

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('generate_students/', generate_students),
    path('generate_teachers/', generate_teachers),
    path('students/', students_list, name='students'),
    path('teachers/', teachers_list, name='teachers'),
    path('groups/', groups_list, name='groups'),
    path('students/add', students_add),
    path('teachers/add', teachers_add),
    path('groups/add', groups_add),
    path('students/edit/<int:id>', students_edit),
    path('students/delete/<int:id>', students_delete),
    path('teachers/edit/<int:id>', teachers_edit),
    path('groups/edit/<int:id>', groups_edit),
    path('', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
