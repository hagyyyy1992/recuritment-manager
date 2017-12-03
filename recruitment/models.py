from django.contrib.auth.models import User
from django.db import models

class Recruitment(models.Model):
    name = models.CharField('氏名', max_length=255)
    email = models.EmailField('連絡先')
    school_name = models.CharField('学校名', max_length=255)
    department = models.CharField('学部', max_length=255)
    school_year = models.IntegerField('学年',null=True)
    age = models.IntegerField('年齢',null=True)
    graduation_year = models.IntegerField('卒業年度',null=True)
    candidates_accuracy = models.IntegerField('確度（採用候補側）',null=True)
    accuracy_reason = models.CharField('確度理由', max_length=255)
    desired_degree = models.IntegerField('欲しい度合い',null=True)
    competition = models.CharField('迷っている会社（競合）', max_length=255)
    selection_phase = models.CharField('フェーズ', max_length=255)
    selection_status = models.CharField('選考状況', max_length=255)
    graduation_flg = models.IntegerField('卒業フラグ',null=True)
    resume_flg = models.IntegerField('履歴書受領フラグ',null=True)
    hiring_fee = models.IntegerField('採用フィー',null=True)
    delete_flg = models.IntegerField('削除フラグ', null=True, default=0)
    agreement_flg = models.IntegerField('内定承諾フラグ',null=True)
    created_date = models.DateTimeField('作成日時', auto_now_add=True)
    update_date = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name

class Interview(models.Model):

    date = models.DateField('面接日')
    time = models.TimeField('時間')
    interviewer = models.CharField('面接官', max_length=255)

    def __str__(self):
        return self.interviewer