from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
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

    # def create(self):
    #     user = User()
    #     form = UserCreateForm(user.POST, instance=user)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('accounts/user_create_done.html'))
