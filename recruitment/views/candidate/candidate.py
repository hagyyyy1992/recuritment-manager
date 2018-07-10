from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

from recruitment.forms import RecruitmentForm
from recruitment.model.models import Recruitment, ArchiveList


# 採用候補者一覧画面表示
@login_required
def candidate_list(request):
    context = \
        {
            # 素の SQL を記述
            'candidates': Recruitment.objects.raw
            (
                'SELECT '
                'recruitment_recruitment.id, recruitment_recruitment.name, recruitment_recruitment.email, '
                'recruitment_recruitment.school_name, recruitment_recruitment.department, '
                'recruitment_recruitment.school_year, recruitment_recruitment.age, '
                'recruitment_recruitment.graduation_year, recruitment_recruitment.candidates_accuracy, '
                'MAX(recruitment_interview.date) AS max_date '
                
                'FROM '
                'recruitment_recruitment '
                
                'LEFT JOIN '
                'recruitment_interview ON recruitment_recruitment.id = recruitment_interview.recruitment_id '
                
                'GROUP BY '
                'recruitment_recruitment.id,recruitment_interview.recruitment_id,recruitment_recruitment.delete_flg '
                
                # delete_flgが0のもののみ表示する
                'HAVING '
                'recruitment_recruitment.delete_flg = 0'
            )
        }
    return TemplateResponse(request, 'candidate/candidate_list.html', context=context)


# アーカイブ画面に移動させる
@login_required
@require_POST
def add_to_archive_list(request, candidate_id):
    # idに紐づくRecruitmentレコードを取得
    recruitment = get_object_or_404(Recruitment, pk=candidate_id)
    # アーカイブリストを作成
    archive_list, created = ArchiveList.objects.get_or_create(user=request.user)
    # アーカイブリストに対象を追加
    archive_list.recruitment.add(recruitment)
    # アーカイブ追加の時はdelete_flgを1にする
    recruitment.delete_flg = 1
    recruitment.save()
    return HttpResponseRedirect(reverse('archive_list'))


# 採用候補者編集画面
@login_required
def edit(request, candidate_id):
    candidate = get_object_or_404(Recruitment, pk=candidate_id)
    if request.method == 'POST':
        form = RecruitmentForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('candidate_list'))
    else:
        form = RecruitmentForm(instance=candidate)

    context = {'form': form, 'candidate': candidate}
    return TemplateResponse(request, 'candidate/candidate_edit.html', context=context)
