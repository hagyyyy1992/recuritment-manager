from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views import generic

from recruitment.forms import UserCreateForm

User = get_user_model()


class UserCreate(generic.CreateView):
    """ユーザー仮登録"""
    template_name = 'accounts/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        return redirect('user_create_done')


class UserCreateDone(generic.TemplateView):
    """ユーザー登録したよ"""
    template_name = 'accounts/user_create_done.html'
