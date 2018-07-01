from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse

from recruitment.forms import InterviewForm, RecruitmentForm
from recruitment.models import Interview, Recruitment


# 面接日程追加機能
@login_required
def add_to_interview(request, candidate_id):
    interview = Interview()
    if request.method == 'POST':
        form = InterviewForm(
            request.POST,
            initial={'recruitment': candidate_id}
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('candidate_list'))
    else:
        form = InterviewForm(
            initial={'recruitment': candidate_id}
        )

    context = {'form': form, 'interview': interview}
    return TemplateResponse(request, 'interview/interview_add.html', context=context)
