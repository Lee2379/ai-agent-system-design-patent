# Technical drawing index / 技術図面一覧

[English portfolio](../README.md) · [日本語ポートフォリオ](../japanese-readme.md)

Six monochrome drawing sheets explain the architecture, agent responsibilities, and operating procedures. Each sheet uses consistent line weights, orthogonal connections, and reference numerals, with a matching Japanese version.

These are portfolio explanatory drawings based on the [provided specification](../source/specification.txt). They are **not original filed or issued patent drawings**. The layout and reference numerals were created for this portfolio. Dashed enclosures in Figure 6 identify additional implementation proposals.

全6種の白黒図面で、構成、エージェントの役割、運用手順を説明します。線の太さ、直交する接続線、構成要素の符号を統一し、英語版と日本語版を用意しています。

図は[提供された明細書](../source/specification.txt)に基づくポートフォリオ用説明図であり、**出願時または登録時の原図ではありません**。配置と符号は本資料用に作成したものです。図6の破線内は、実装に向けた追加の提案を示します。

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

S10–S60 identify delivery steps. A–C identify separate safety scenarios. Neither notation is an original claim identifier.

S10〜S60は配送手順、A〜Cは独立した異常シナリオを表します。いずれも元の請求項番号ではありません。

## Rebuild / 再生成

All 12 SVGs are generated using Python 3 and its standard library:

全12点のSVGはPython 3の標準ライブラリのみで再生成できます。

```bash
python scripts/build_visuals.py
```

The SVGs contain editable text, accessibility titles, and descriptions. They have no external resources, embedded screenshots, or personal names.

SVGには編集可能な文字、アクセシビリティ用のタイトルと説明を含めています。外部リソース、埋め込みスクリーンショット、個人の氏名は含めていません。
