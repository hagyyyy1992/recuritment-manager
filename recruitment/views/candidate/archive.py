from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

from recruitment.forms import RecruitmentForm
from recruitment.model.models import Recruitment, ArchiveList


# アーカイブ画面表示
@login_required
def archive_list(request):
    archive_list, created = ArchiveList.objects.get_or_create(user=request.user)
    context = {'candidates': archive_list.recruitment.all()}
    return TemplateResponse(request, 'candidate/candidate_archive_list.html', context=context)

# アーカイブ編集
@login_required
def edit(request, candidate_id):
    candidate = get_object_or_404(Recruitment, pk=candidate_id)
    if request.method == 'POST':
        form = RecruitmentForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('archive_list'))
    else:
        form = RecruitmentForm(instance=candidate)

    context = {'form': form, 'candidate': candidate}
    return TemplateResponse(request, 'candidate/candidate_archive_edit.html', context=context)

# 採用候補者削除
@login_required
@require_POST
def delete(request, candidate_id):
    candidate = get_object_or_404(Recruitment, pk=candidate_id)
    candidate.delete()
    return HttpResponseRedirect(reverse('archive_list'))

# 採用候補者一覧に戻す
@login_required
@require_POST
def return_to_candidate_list(request, candidate_id):
    # idに紐づくRecruitmentレコードを取得
    recruitment = get_object_or_404(Recruitment, pk=candidate_id)
    # アーカイブリストを作成
    archive_list, created = ArchiveList.objects.get_or_create(user=request.user)
    # 対象を削除
    archive_list.recruitment.remove(recruitment)
    # アーカイブから戻す時はdelete_flgを0にする
    recruitment.delete_flg = 0
    recruitment.save()
    return HttpResponseRedirect(reverse('candidate_list'))
