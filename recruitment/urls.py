from django.urls import re_path
from recruitment.views.candidate import candidate, archive, candidate_add, interview_add
from recruitment.views.accounts import user

urlpatterns = [
    # ユーザー作成画面
    re_path(r'^user_create/$', user.UserCreate.as_view(), name='user_create'),
    # ユーザー作成完了画面
    re_path(r'^user_create/done/$', user.UserCreateDone.as_view(), name='user_create_done'),
    # 選考者一覧画面
    re_path(r'^$', candidate.candidate_list, name='candidate_list'),
    # 選考者編集画面
    re_path(r'^(?P<candidate_id>[0-9]+)/candidate_edit/$', candidate.edit, name='candidate_edit'),
    # アーカイブ編集画面
    re_path(r'^(?P<candidate_id>[0-9]+)/candidate_archive_edit/$', archive.edit, name='candidate_archive_edit'),
    # 選考者追加画面
    re_path(r'^candidate_add/$', candidate_add.add_to_candidate_list, name='candidate_add'),
    # 削除ボタン
    re_path(r'^(?P<candidate_id>[0-9]+)/delete/$', archive.delete, name='candidate_archive_delete'),
    # アーカイブ画面
    re_path(r'^archive_list/$', archive.archive_list, name='archive_list'),
    # アーカイブ追加
    re_path(r'^(?P<candidate_id>[0-9]+)/add/archive_list/$', candidate.add_to_archive_list, name='add_archive'),
    # アーカイブ削除
    re_path(r'^(?P<candidate_id>[0-9]+)/return/candidate_list/$', archive.return_to_candidate_list,
            name='return_to_candidate_list'),
    # 選考日程追加
    re_path(r'^(?P<candidate_id>[0-9]+)/interview_add/$', interview_add.add_to_interview, name='interview_add')
]
