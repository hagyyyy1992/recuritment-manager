# recuritment_manager

【作成背景】<br>
きっかけは会社で使ってもらいたいと思って作り始めましたが、色々あって今は個人の趣味開発として拡張を進めています。 

【ツールの目的】<br>
採用の選考者を管理することを目的としたツールです。

【大変だったこと】<br>
制作期間は2017/10~2017/12です。しばらく他の勉強をしていたため最近手直しを入れ始めました。（別アカウントのプライベートリポジトリで作業していたため草は生えていません。。)<br>
苦労したのはDjangoはSQLiteが標準搭載になっているが自分はMySQLで書きたかったのでドライバを入れ直したら、herokuのDBはデフォルトではPostgreSQLなので、MySQLを使おうとすると設定を変更する必要があり、インフラ側の設定変更にあまり詳しくなく時間もなかったので渋々PosgreSQL対応にしたことです。<br>
また一覧取得をDjangoのライブラリで行いたかったのですが保守性の点からも無理がありそうだったのでSQL直書きにした点です。

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
 
## 今後追加したい機能
 - ~~削除機能をまだ作っていません。~~ →　2018/7/1追加<br>
 - ~~登録機能~~ → 2018/7/29追加<br>
 - メール認証機能<br>
 - ログイン情報ごとにアカウントを分ける<br>
 - アカウントごとに権限をつける<br>
 - 過去の面接情報が履歴表示される<br>
 - チャット<br>
 etc...
 
## 使っている技術
 - Python 3.6.3<br>
 - Django 2.0.6<br>
 - heroku<br>
 - PostgreSQL
