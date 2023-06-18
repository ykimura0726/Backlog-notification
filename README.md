# 概要

最初に、lambda_function.py はターミナルから実行するプログラムではない。
このプログラムは、以下の AWS サービスを利用し、Backlog から特定のプロジェクトについて、Slack へ通知を飛ばす関数として、Lambda に保存しているものである。

- AWS Lambda
- Amazon EventBridge
- KMS (AWS Key Management Service)
- AWS IAM

# 注意

このプログラムは就活のため、本来公開する予定のないものをパブリックリポジトリとして一定期間内に限って公開しているものである。  
プログラム中には API キーや URL などの情報があるが、.env に環境変数を定義し、.gitignore ファイルに.env を追加し、Git の追跡対象外としている。  
そのため、このファイルを AWS Lambda でそのまま動かすことはできないという点に留意してほしい。

# 実装にあたって

このプログラムを作成し、テストも通っているものの、残念ながら実際に Slack で運用することはかなわなかった。Backlog に Webhook を追加する権限がないことにプログラム作成後に気づいたためである。Backlog の管理者権限の付与または管理者に Webhook を追加してもらうよう打診する予定である。

# 参考文献

以下は、このプログラム作成にあたって参考とした参考文献である。

- [【Ruby on Rails】GitHub に公開したくない変数や値を隠して push する方法](https://zenn.dev/noraworld/articles/keep-values-a-secret-on-rails)

- [環境変数の代わりに .env ファイルを使用する (dotenv)](https://maku77.github.io/nodejs/env/dotenv.html)

- [Slack アプリ開発を始めるときに全人類が知っておくべきこと](https://www.wantedly.com/companies/wantedly/post_articles/302887#_=_)

- [Backlog タスクの定期チェックと通知を Slack で受け取る方法](https://ops.jig-saw.com/tech-cate/backlog-slack)

- [Backlog 課題一覧の取得(日本語公式サイト)](https://developer.nulab.com/ja/docs/backlog/api/2/get-issue-list/#)

- [Backlog の Webhook を有効化する手順～ Backlog の課題情報を外部連携するために](https://auto-worker.com/blog/?p=459)
