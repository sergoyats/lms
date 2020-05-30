from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView

from user_account.forms import UserAccountRegistrationForm


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserAccountRegistrationForm

    def get_success_url(self):
        return reverse('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context
