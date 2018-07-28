from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from recruitment.model.models import Recruitment, Interview, ArchiveList


class RecruitmentForm(ModelForm):
    class Meta:
        model = Recruitment
        fields = [
            'name',
            'email',
            'school_name',
            'department',
            'school_year',
            'age',
            'graduation_year',
            'selection_status'
        ]


class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = [
            'recruitment',
            'date',
            'time',
            'interviewer'
        ]


class ArchiveList(ModelForm):
    class Meta:
        model = ArchiveList
        fields = [
            'user'
        ]


class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email',)
        else:
            fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
