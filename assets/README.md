# Technical drawing index / 技術図面一覧

[English portfolio](../README.md) · [日本語ポートフォリオ](../japanese-readme.md)

I created these six figures to explain the system architecture and operation, using the same component numbers in English and Japanese. They are explanatory drawings based on the [specification](../source/specification.txt), separate from the official patent drawings. The dashed section in Figure 6 shows a proposed model validation and release process.

システムの構成と動作を説明するため、英語・日本語で6種の図を作成しました。両言語で共通の構成要素番号を使っています。[明細書](../source/specification.txt)に基づく説明図で、正式な特許図面とは別のものです。図6の破線内には、モデルの検証と更新の手順案を示しています。

| Figure / 図 | Subject / 内容 | English | 日本語 |
|---|---|---|---|
| 1 | System architecture / システム全体構成 | [SVG](fig-01-system-architecture-en.svg) | [SVG](fig-01-system-architecture-ja.svg) |
| 2 | AI agent coordination / AIエージェント間の連携 | [SVG](fig-02-agent-coordination-en.svg) | [SVG](fig-02-agent-coordination-ja.svg) |
| 3 | Delivery procedure / 配送手順 | [SVG](fig-03-delivery-sequence-en.svg) | [SVG](fig-03-delivery-sequence-ja.svg) |
| 4 | Drone functional components / ドローンの機能構成 | [SVG](fig-04-drone-components-en.svg) | [SVG](fig-04-drone-components-ja.svg) |
| 5 | Safety response scenarios / 異常時の応答 | [SVG](fig-05-safety-responses-en.svg) | [SVG](fig-05-safety-responses-ja.svg) |
| 6 | Operational data and AI improvement / 運用データとAIの改善 | [SVG](fig-06-learning-flow-en.svg) | [SVG](fig-06-learning-flow-ja.svg) |

## Reference numerals / 構成要素の符号

| Reference / 符号 | English | 日本語 |
|---|---|---|
| 110 | Customer platform | 顧客プラットフォーム |
| 120 | Central AI control server | 中央AI制御サーバー |
| 121 | Hierarchical AI agents | 階層型AIエージェント |
| 122 | Network AI agents | ネットワーク型AIエージェント |
| 130 | Satellite communication | 衛星通信 |
| 140 | Autonomous drone / fleet | 自律型ドローン・機体群 |
| 141 | GPS positioning | GPS測位 |
| 142 | Object-detection sensors | 物体検知センサー |
| 143 | Cameras | カメラ |
| 144 | Communication modules | 通信モジュール |
| 145 | Electric propulsion | 電動推進 |
| 150 | Encrypted cloud database | 暗号化クラウドDB |
| 160 | AI improvement | AIの改善 |
| 170 | Designated delivery point | 指定受取地点 |

S10–S60 mark the delivery steps; A–C mark the safety scenarios.

S10〜S60は配送手順、A〜Cは異常時のシナリオを表します。

## Rebuild / 再生成

All 12 SVGs are generated using Python 3 and its standard library:

全12点のSVGはPython 3の標準ライブラリのみで再生成できます。

```bash
python scripts/build_visuals.py
```

The SVG files use editable text and include accessible titles and descriptions. No external resources are required.

SVGの文字は編集可能です。アクセシビリティ用のタイトルと説明を含み、外部リソースを使わずに表示できます。
