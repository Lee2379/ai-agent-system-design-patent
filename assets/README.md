# Visual assets / 図版一覧

[English portfolio](../README.md) · [日本語ポートフォリオ](../japanese-readme.md)

All figures are explanatory illustrations prepared from the [provided specification](../source/specification.txt) and the clearly labeled implementation considerations in the system-design documents. The landscape is conceptual; routes and positions do not represent a real flight or geographic service area.

すべての図は、[提供された明細書](../source/specification.txt)と、システム設計文書に明示した実装上の検討事項に基づく説明図です。地形・経路・位置は概念的な表現であり、実際の飛行やサービス提供地域を示すものではありません。

| Figure / 図 | English | 日本語 |
|---|---|---|
| 01 · Delivery environment / 配送環境 | [SVG](delivery-context-en.svg) | [SVG](delivery-context-ja.svg) |
| 02 · System architecture / システム構成 | [SVG](architecture-en.svg) | [SVG](architecture-ja.svg) |
| 03 · Agent coordination / エージェント連携 | [SVG](agent-coordination-en.svg) | [SVG](agent-coordination-ja.svg) |
| 04 · Delivery lifecycle / 配送フロー | [SVG](delivery-flow-en.svg) | [SVG](delivery-flow-ja.svg) |
| 05 · Safety responses / 安全動作 | [SVG](safety-responses-en.svg) | [SVG](safety-responses-ja.svg) |
| 06 · Operational learning / 運用データの学習利用 | [SVG](learning-cycle-en.svg) | [SVG](learning-cycle-ja.svg) |

Figures 01, 03, 05, and 06 can be regenerated from the repository root using Python 3 and its standard library:

図01・03・05・06は、リポジトリのルートで次のコマンドを実行すると再生成できます。Python 3の標準ライブラリのみを使用します。

```bash
python scripts/build_visuals.py
```

The SVGs contain editable text, accessibility titles, and descriptions. No external fonts, tracking resources, personal names, or embedded screenshots are included.

SVGには編集可能なテキスト、アクセシビリティ用のタイトルと説明を含めています。外部フォント、追跡用リソース、個人の氏名、埋め込みスクリーンショットは使用していません。
