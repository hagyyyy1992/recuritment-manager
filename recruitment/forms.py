from django.forms import ModelForm

from recruitment.models import Recruitment,Interview,ArchiveList


class RecruitmentForm(ModelForm):
    class Meta:
        model = Recruitment
        fields = [
            'name', 'email', 'school_name', 'department',
            'school_year', 'age', 'graduation_year', 'selection_status'
        ]

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = [
            'recruitment','date', 'time', 'interviewer'
        ]

class ArchiveList(ModelForm):
    class Meta:
        model = ArchiveList
        fields = ['user']