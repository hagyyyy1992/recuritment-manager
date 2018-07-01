from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from recruitment.forms import RecruitmentForm
from recruitment.model.models import Recruitment


# 採用候補者追加
@login_required
def add_to_candidate_list(request):
    candidate = Recruitment()
    if request.method == 'POST':
        form = RecruitmentForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('candidate_list'))
    else:
        form = RecruitmentForm(instance=candidate)

    context = {'form': form, 'candidate': candidate}
    return TemplateResponse(request, 'candidate/candidate_add.html', context=context)
