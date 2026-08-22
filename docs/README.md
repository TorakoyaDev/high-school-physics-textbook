# 制作ドキュメント案内

このディレクトリには、本文そのものではなく「どのような本を、どのように作るか」を残す。

## 構成

- [`book-plan.md`](book-plan.md)：書籍全体の構成、読者像、数学方針
- [`chapters/`](chapters/)：各章の到達目標、節構成、問題配置
- [`editorial/style-guide.md`](editorial/style-guide.md)：文章と教材設計の共通原則
- [`editorial/review-checklist.md`](editorial/review-checklist.md)：ビルド・公開前の確認
- [`editorial/feedback-log.md`](editorial/feedback-log.md)：ユーザーの指摘から得た学び
- [`reference/`](reference/)：初期メモや、本文へ落とす前の技術的考察
- [`build-and-publish-policy.md`](build-and-publish-policy.md)：ビルド、レビュー、公開方法

## 学びを蓄積する流れ

```text
読者・ユーザーからの指摘
  → 該当箇所を直す
  → 同種の箇所を横断検索する
  → feedback-log に事実と学びを残す
  → 一般化できる場合だけ style-guide / checklist を更新する
  → 次の章へ適用する
```

`feedback-log.md` は単なる変更履歴ではない。「何が読みにくかったか」「なぜ起きたか」「今後どう防ぐか」を残す。

