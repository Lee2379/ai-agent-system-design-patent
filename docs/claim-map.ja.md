# 請求項と設計の対応

[ポートフォリオ](../japanese-readme.md) · [English](claim-map.md) | 日本語

## 本表の読み方

[提供された明細書](../source/specification.txt)の請求項には、基本構成と「claim 1」を参照する四つの記述があります。以下のC1〜C5は、それらを整理するための番号です。本表は提供された文章の技術的な対応関係をまとめたもので、登録特許の文言や権利範囲を確定するものではありません。

## 提供文書内の請求項

| 整理番号 | 内容の要約 | 対応する説明箇所 | ポートフォリオでの表現 |
|---|---|---|---|
| **C1** | GPS、センサー、通信モジュールを持つドローンと、衛星通信によるAIの自律配送管理 | Summary of the Invention、Detailed DescriptionのSystem ArchitectureおよびCommunication Framework | AI制御系、通信層、自律型機体群 |
| **C2** | 階層型エージェントによる運航計画と経路の調整 | Summary of the Invention、System Architecture、AI Agent Operation | 階層型エージェントの責任表、機体割当・経路計画 |
| **C3** | ネットワーク型エージェントによる機体・顧客間のリアルタイム通信 | Summary of the Invention、Communication Framework | ネットワーク型エージェントの責任表、状態共有・通知 |
| **C4** | 到着前にAIが自動配送通知を送信 | System Operationの手順4、Product Delivery Processの手順3 | 到着前通知。説明本文では到着約5分前と記載 |
| **C5** | 運用データの将来の改善への利用と電動ドローン | System Operationの手順6、Key Advantages、Learning and Optimization | 運用データの活用サイクルと電動機体 |

## 請求項の要約以外に説明本文で記載されている事項

| 機能 | 記載箇所 | 本資料での扱い |
|---|---|---|
| カメラ画像と暗号化クラウド保存 | System Architecture、Learning and Optimization | データ収集・保存の設計 |
| 経路計画と障害物回避の深層学習 | AI Agent Operation | 原文にあるAI手法。モデル構成・学習手順は未指定 |
| 暗号化・認証・耐量子通信 | Communication Framework | 説明本文のセキュリティ要件。実装・検証済みとは記載しない |
| 通信の冗長化、異常時の帰還・着陸 | Safety Considerations | 安全動作と実装上の検討事項 |
| 地上の配送区画・指定された窓 | System Operationの手順5 | 受取地点の例。荷物の解放機構は仮定しない |
| 医療物流、災害対応、エアタクシー | Applications and Extensions | 提案された応用方向 |

## 出典の範囲

- ポートフォリオの表題は説明用です。正式名称と書誌識別情報は[特許情報](patent-record.ja.md)に記載しています。
- 添付の明細書は技術的な本文です。書誌情報には、別途提供された特許参照先とGoogle Patentsの現行情報を利用しています。
- 特許図面、試作結果、飛行ログ、実行可能なコード、実測の性能表は添付されていません。
- 構成図と実装上の検討事項は、ポートフォリオ向けに作成した説明資料です。
- 提供された原文は`source/specification.txt`に変更せず保存しています。英文の編集と日本語訳はポートフォリオ文書に適用しています。

出典と書誌情報の参照先は[特許情報](patent-record.ja.md)を参照してください。
