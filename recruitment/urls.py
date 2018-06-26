from django.conf.urls import url
from recruitment.views.candidate import candidate, archive, candidate_add, interview_add

urlpatterns = [
    # 選考者一覧画面
    url(r'^$', candidate.candidate_list, name='candidate_list'),
    # 選考者編集画面
    url(r'^(?P<candidate_id>[0-9]+)/candidate_edit/$', candidate.edit, name='candidate_edit'),
    # アーカイブ編集画面
    url(r'^(?P<candidate_id>[0-9]+)/candidate_edit/$', candidate.edit, name='candidate_edit'),
    # 選考者追加画面
    url(r'^candidate_add/$', candidate_add.add_to_candidate_list, name='candidate_add'),
    # 削除ボタン
    url(r'^(?P<candidate_id>[0-9]+)/delete/$', archive.delete, name='candidate_delete'),
    # アーカイブ画面
    url(r'^archive_list/$', archive.archive_list, name='archive_list'),
    # アーカイブ追加
    url(r'^(?P<candidate_id>[0-9]+)/add/archive_list/$', candidate.add_to_archive_list, name='add_archive'),
    # アーカイブ削除
    url(r'^(?P<candidate_id>[0-9]+)/return/candidate_list/$', archive.return_to_candidate_list, name='return_to_candidate_list'),
    # 選考日程追加
    url(r'^interview_add/$', interview_add.add_to_interview, name='interview_add')
]