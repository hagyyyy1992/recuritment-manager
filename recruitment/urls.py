from django.conf.urls import url
from recruitment import views

urlpatterns = [
    url(r'^$', views.candidate_list, name='candidate_list'),  # 選考者一覧画面
    url(r'^(?P<candidate_id>[0-9]+)/candidate_edit/$', views.edit, name='candidate_edit'),  # 選考者編集画面
    url(r'^candidate_add/$', views.add_to_candidate_list, name='candidate_add'),  # 選考者追加画面
    url(r'^(?P<candidate_id>[0-9]+)/delete/$', views.delete, name='candidate_delete'),  # 削除ボタン
    url(r'^archive_list/$', views.archive_list, name='archive_list'),  # アーカイブ画面
    url(r'^(?P<candidate_id>[0-9]+)/add/archive_list/$', views.add_to_archive_list, name='add_archive'),  # アーカイブ追加
    url(r'^(?P<candidate_id>[0-9]+)/return/candidate_list/$', views.return_to_candidate_list, name='return_to_candidate_list')  # アーカイブ削除
]