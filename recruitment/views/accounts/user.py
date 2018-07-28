from django.urls import reverse_lazy
from django.views import generic

from recruitment.forms import UserCreateForm


class UserCreate(generic.CreateView):
    """ユーザー登録"""
    template_name = 'accounts/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user_create_done')


class UserCreateDone(generic.TemplateView):
    """ユーザー登録完了"""
    template_name = 'accounts/user_create_done.html'
