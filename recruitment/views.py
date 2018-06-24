from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST

from recruitment.forms import RecruitmentForm, InterviewForm
from recruitment.models import Recruitment, ArchiveList, Interview


# 採用候補者一覧画面表示
@login_required
def candidate_list(request):
    context = \
        {
            'candidates': Recruitment.objects.raw
                (
                # delete_flgが0のもののみ表示する
                'SELECT '
                'recruitment_recruitment.id, '
                'recruitment_recruitment.name, '
                'recruitment_recruitment.email, '
                'recruitment_recruitment.school_name, '
                'recruitment_recruitment.department, '
                'recruitment_recruitment.school_year, '
                'recruitment_recruitment.age, '
                'recruitment_recruitment.graduation_year, '
                'recruitment_recruitment.candidates_accuracy, '
                'MAX(recruitment_interview.date) AS max_date '
                'FROM recruitment_recruitment '
                'LEFT JOIN recruitment_interview '
                'ON recruitment_recruitment.id = recruitment_interview.recruitment_id '
                'GROUP BY recruitment_recruitment.id,'
                'recruitment_interview.recruitment_id,'
                'recruitment_recruitment.delete_flg '
                'HAVING recruitment_recruitment.delete_flg = 0'

            )
        }
    return TemplateResponse(request, 'candidate/candidate_list.html', context=context)


# アーカイブ画面表示
@login_required
def archive_list(request):
    archive_list, created = ArchiveList.objects.get_or_create(user=request.user)
    context = {'candidates': archive_list.recruitment.all()}
    return TemplateResponse(request, 'candidate/candidate_archive_list.html', context=context)


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


# 採用候補者削除
@login_required
@require_POST
def delete(request, candidate_id):
    candidate = get_object_or_404(Recruitment, pk=candidate_id)
    candidate.delete()
    return HttpResponseRedirect(reverse('candidate_list'))


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
