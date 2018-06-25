from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from recruitment.forms import InterviewForm
from recruitment.models import Interview


# 面接日程追加機能
@login_required
def add_to_interview(request):
    interview = Interview()
    if request.method == 'POST':
        form = InterviewForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('candidate_list'))
    else:
        form = InterviewForm(instance=interview)

    context = {'form': form, 'interview': interview}
    return TemplateResponse(request, 'interview/interview_add.html', context=context)
