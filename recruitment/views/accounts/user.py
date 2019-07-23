from django.urls import reverse_lazy
from django.views import generic

from recruitment.forms import UserCreateForm

# ユーザー登録
class UserCreate(generic.CreateView):
    template_name = 'accounts/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user_create_done')

# ユーザー登録完了
class UserCreateDone(generic.TemplateView):
    template_name = 'accounts/user_create_done.html'
