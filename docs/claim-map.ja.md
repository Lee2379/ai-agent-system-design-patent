# 請求項と設計の対応

[ポートフォリオ](../japanese-readme.md) · [English](claim-map.md) | 日本語

## 請求項と設計

[明細書](../source/specification.txt)の五つの請求項記述をC1〜C5で表し、関連する設計要素を整理しました。以下は技術的な要約です。請求項の正式な文言は特許文書を参照してください。

## 請求項の概要

| 整理番号 | 内容の要約 | 対応する説明箇所 | 対応する設計要素 |
|---|---|---|---|
| **C1** | GPS、センサー、通信モジュールを持つドローンと、衛星通信によるAIの自律配送管理 | Summary of the Invention、Detailed DescriptionのSystem ArchitectureおよびCommunication Framework | AI制御系、通信層、自律型機体群 |
| **C2** | 階層型エージェントによる運航計画と経路の調整 | Summary of the Invention、System Architecture、AI Agent Operation | 階層型エージェントの責任表、機体割当・経路計画 |
| **C3** | ネットワーク型エージェントによる機体・顧客間のリアルタイム通信 | Summary of the Invention、Communication Framework | ネットワーク型エージェントの責任表、状態共有・通知 |
| **C4** | 到着前にAIが自動配送通知を送信 | System Operationの手順4、Product Delivery Processの手順3 | 到着前通知。説明本文では到着約5分前と記載 |
| **C5** | 運用データの将来の改善への利用と電動ドローン | System Operationの手順6、Key Advantages、Learning and Optimization | 運用データの活用サイクルと電動機体 |

## 詳細な説明に含まれる機能

| 機能 | 記載箇所 | 設計内容と検討事項 |
|---|---|---|
| カメラ画像と暗号化クラウド保存 | System Architecture、Learning and Optimization | データ収集・保存の設計 |
| 経路計画と障害物回避の深層学習 | AI Agent Operation | 深層学習を利用。モデル構成と学習手順は今後具体化 |
| 暗号化・認証・耐量子通信 | Communication Framework | セキュリティ要件。プロトコルの選定と試験は実装段階で実施 |
| 通信の冗長化、異常時の帰還・着陸 | Safety Considerations | 安全動作と実装上の検討事項 |
| 地上の配送区画・指定された窓 | System Operationの手順5 | 受取地点の選択肢。荷物の解放機構は詳細設計で検討 |
| 医療物流、災害対応、エアタクシー | Applications and Extensions | 提案された応用方向 |

## 関連資料

[システム設計](system-design.ja.md)では、特許の記述を踏まえた実装案と評価方法を検討しています。登録情報と関連ファイルは[特許情報](patent-record.ja.md)にまとめています。
