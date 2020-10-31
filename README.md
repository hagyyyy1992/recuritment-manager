# 環境構築

```
$ git clone git@github.com:kqxgy385/recuritment-manager.git
$ cd recuritment-manager
$ python -m venv venv
$ source ./venv/bin/activate
$ brew install psycopg2
$ export LDFLAGS="-L/usr/local/opt/openssl/lib"
$ export CPPFLAGS="-I/usr/local/opt/openssl/include"
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
$ python manage.py makemigrations recruitment
$ python manage.py migrate
$ python manage.py runserver
```

http://127.0.0.1:8000/accounts/login/

# recuritment_manager

【作成背景】<br>
きっかけは会社で使ってもらいたいと思って作り始めました。<br>
現在は個人の趣味開発として拡張を進めています。 

【ツールの目的】<br>
採用の選考者を管理することを目的としたツールです。<br>
制作期間は2017/10〜2017/12、2018/06〜2018/07です。

【苦労した点】<br>
- DjangoはSQLiteが標準搭載になっているが、PosgreSQL対応に変更した点（本当はMySQLで行いたかったが時間的なコストの観点でPosgreSQLで対応しました。）
- 一覧取得をDjangoのライブラリで行いたかったのですが保守性の点からも無理がありそうだったのでSQL直書きにした点

【ログイン情報】<br>
画面右上アカウント登録から登録したら、登録したユーザー名とパスワードで入れます。<br>
または以下でもログインできます。<br>
ID: u13641 <br>
Pass: dreU1tZJ

https://test-app-20180622005216.herokuapp.com/accounts/login/

## 主な画面
### アカウント登録画面
 - ユーザー名、メールアドレス、パスワードを入力します
 - メールアドレスにはdjangoのメールアドレスクラスの最低限のバリデーションが入っています
 - パスワードはdjangoのパスワードクラスの最低限のバリデーションが入っています
 - 送信を押すと登録完了画面に遷移できます。

### 採用候補者一覧
 - 各カラムソートができます<br>
 - IDをクリックすると更新に遷移します。<br>
 - 「アーカイブに移動する」でアーカイブに遷移します。<br>
 - 「選考日程を追加する」で選考日程追加画面に遷移できます。

### 採用候補者更新
 - 採用候補者一覧から遷移します<br>
 - 選考者情報を更新できます。更新ボタンを押すと採用候補者一覧に遷移します。<br>
 - 連絡先は@以降を入力しないとバリデーションエラーになります

### 採用候補者追加
 - 新規選考者を追加できます
 
### 選考日程追加
 - 採用候補者更新から遷移できます
 - 候補者の日程を更新できます<br>
 - 候補者名で選択できます

### 過去選考者一覧
 - 一覧から遷移できます<br>
 - 「一覧に戻す」でアーカイブから消すことができます
 
### 過去選考者更新
 - 過去選考者一覧から遷移します<br>
 - 選考者情報を更新できます<br>
 - 連絡先は@以降を入力しないとバリデーションエラーになります<br>
 - 削除できます。削除ボタンを押すとデータが物理削除され過去選考者一覧に遷移します。

### その他機能
 - アーカイブ削除機能
 - ユーザー登録機能
 
## 今後追加したい機能
 - メール認証機能<br>
 - ログイン情報ごとにアカウントを分ける<br>
 - アカウントごとに権限をつける<br>
 - 過去の面接情報が履歴表示される<br>
 - チャット<br>
 etc...
 
## 使っている技術
 - Python 3.9.0<br>
 - Django 3.1.2<br>
 - heroku<br>
 - PostgreSQL
