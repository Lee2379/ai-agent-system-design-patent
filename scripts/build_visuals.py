"""Build bilingual explanatory drawings with Python's standard library.

Reference numerals are editorial aids, not numbers from filed patent drawings.
The figures describe functional relationships, not mechanical construction.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'assets'
FONT = "Arial, 'Yu Gothic', Meiryo, sans-serif"


def text(x, y, value, size=22, anchor='middle', bold=False):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{600 if bold else 400}" '
            f'fill="#111">{escape(value)}</text>')


def lines(x, y, values, size=22, step=31, **kwargs):
    return ''.join(text(x, y + i * step, v, size, **kwargs) for i, v in enumerate(values))


def rect(x, y, w, h, dashed=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'fill="white" stroke="#111" stroke-width="1.8"'
            + (' stroke-dasharray="9 6"' if dashed else '') + '/>')


def line(d, arrow=False, both=False, dashed=False):
    return (f'<path d="{d}" fill="none" stroke="#111" stroke-width="1.8" stroke-linejoin="miter"'
            + (' marker-end="url(#arrow)"' if arrow or both else '')
            + (' marker-start="url(#start)"' if both else '')
            + (' stroke-dasharray="7 6"' if dashed else '') + '/>')


def block(x, y, w, h, ref, labels, size=22):
    top = y + (h - 27 - len(labels) * 31) / 2 + 22
    return rect(x, y, w, h) + text(x + w / 2, top, ref, 20, bold=True) + lines(x + w / 2, top + 32, labels, size)


def sheet(slug, num, title, body, height, lang, notes):
    desc = ('Explanatory drawing based on the supplied specification. Editorial reference numerals; '
            'not an original patent-office drawing.' if lang == 'en' else
            '提供された明細書に基づく説明図。符号は本資料用の整理番号であり、特許庁の原図ではありません。')
    footer = 'Portfolio explanatory drawing' if lang == 'en' else 'ポートフォリオ用説明図'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" '
           f'viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc" xml:lang="{lang}">'
           f'<title id="title">FIG. {num} — {escape(title)}</title><desc id="desc">{escape(desc)}</desc>'
           '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
           '<path d="M1 1 L9 5 L1 9" fill="none" stroke="#111" stroke-width="1.3"/></marker>'
           '<marker id="start" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
           '<path d="M9 1 L1 5 L9 9" fill="none" stroke="#111" stroke-width="1.3"/></marker></defs>'
           f'<rect width="1120" height="{height}" fill="white"/>'
           + text(56, 43, 'AI AGENT / SYSTEM DESIGN', 16, 'start')
           + text(1064, 43, f'{num} / 6', 16, 'end') + line('M56 60 H1064') + body
           + lines(56, height - 147, notes, 17, 26, anchor='start')
           + line(f'M56 {height - 99} H1064')
           + text(560, height - 61, f'FIG. {num}   {title}', 24, bold=True)
           + text(560, height - 28, footer, 16) + '</svg>\n')
    (OUT / f'fig-{num:02d}-{slug}-{lang}.svg').write_text(svg, encoding='utf-8')


def architecture(lang):
    ja = lang == 'ja'
    s = block(380, 100, 360, 95, '110', ['顧客プラットフォーム' if ja else 'Customer platform'])
    s += line('M535 195 V273', arrow=True) + line('M585 273 V195', arrow=True)
    s += text(515, 237, '注文' if ja else 'Order', 18, 'end')
    s += text(607, 237, '通知' if ja else 'Alert', 18, 'start')
    s += rect(260, 275, 600, 220)
    s += text(560, 313, '120  中央AI制御サーバー' if ja else '120  Central AI control server', 23)
    s += block(285, 340, 245, 125, '121', ['階層型AIエージェント', '割当・運航計画・経路'] if ja else ['Hierarchical AI agents', 'Assignment / routing'], 20)
    s += block(590, 340, 245, 125, '122', ['ネットワーク型AI', 'エージェント・情報共有'] if ja else ['Network AI agents', 'Coordination / exchange'], 20)
    s += line('M530 402 H590', both=True) + line('M550 495 V575', both=True)
    s += block(380, 575, 340, 95, '130', ['衛星通信' if ja else 'Satellite communication'])
    s += line('M550 670 V750', both=True)
    s += block(380, 750, 340, 95, '140', ['自律型ドローン群' if ja else 'Autonomous drone fleet'])
    s += block(65, 750, 235, 95, '170', ['指定受取地点' if ja else 'Delivery point'])
    s += line('M380 798 H300', arrow=True)
    s += block(835, 575, 235, 125, '150', ['暗号化クラウドDB', '運用記録'] if ja else ['Encrypted cloud DB', 'Operational records'], 20)
    s += line('M860 385 H952 V575', arrow=True)
    s += text(970, 490, '保存' if ja else 'Store', 18, 'start')
    s += block(835, 750, 235, 95, '160', ['AIの改善' if ja else 'AI improvement'], 21)
    s += line('M952 700 V750', arrow=True)
    notes = (['矢印は機能上の情報・配送の流れを示します。ネットワーク配線を指定するものではありません。',
              'GPS測位は図4に示します。エージェントの物理的な配置は原文では未指定です。'] if ja else
             ['Arrows show functional exchanges and delivery; they do not prescribe network wiring.',
              'GPS positioning is shown in Fig. 4. Physical placement of agents is unspecified in the source.'])
    sheet('system-architecture', 1, 'システム全体構成' if ja else 'System architecture', s, 1090, lang, notes)


def coordination(lang):
    ja = lang == 'ja'
    xs = [165, 430, 690, 955]
    labels = ([['顧客', 'プラットフォーム'], ['階層型AI', 'エージェント'], ['ネットワーク型AI', 'エージェント'], ['自律型', 'ドローン']] if ja else
              [['Customer', 'platform'], ['Hierarchical AI', 'agents'], ['Network AI', 'agents'], ['Autonomous', 'drone']])
    s = ''
    for x, ref, label in zip(xs, ['110', '121', '122', '140'], labels):
        s += block(x - 110, 105, 220, 118, ref, label, 21)
        s += line(f'M{x} 223 V915', dashed=True)
    events = [(0, 1, 285, 'Delivery request / destination', '配送要求・目的地'),
              (1, 2, 365, 'Assignment / route', '機体割当・経路'),
              (2, 3, 445, 'Mission guidance', '航行指示'),
              (3, 2, 525, 'Position / status', '位置・機体状態'),
              (2, 1, 605, 'Coordination data', '調整に必要な情報'),
              (1, 2, 685, 'Revised guidance', '誘導情報の更新'),
              (2, 3, 765, 'Guidance update', '更新された誘導情報'),
              (2, 0, 870, 'Pre-arrival alert (approximately 5 min)', '到着前通知（約5分前）')]
    for a, b, y, en, jp in events:
        s += line(f'M{xs[a]} {y} H{xs[b]}', arrow=True)
        if abs(b - a) > 1:
            s += f'<rect x="{min(xs[a], xs[b]) + 8}" y="{y-36}" width="{abs(xs[b]-xs[a])-16}" height="27" fill="white"/>'
        s += text((xs[a] + xs[b]) / 2, y - 13, jp if ja else en, 18)
    notes = (['概念的な通信順序。飛行中の状態報告と誘導更新は必要に応じて繰り返します。',
              '通信層は省略しています。API、メッセージ形式、厳密な処理順序は未指定です。'] if ja else
             ['Illustrative exchange sequence. Status reporting and guidance updates recur during flight.',
              'Communication transport is omitted. APIs, message formats, and exact ordering are unspecified.'])
    sheet('agent-coordination', 2, 'AIエージェント間の連携' if ja else 'AI agent coordination', s, 1140, lang, notes)


def delivery(lang):
    ja = lang == 'ja'
    values = ([['配送要求を受信'], ['配送先を確認', '機体を割り当て、経路を計画'], ['GPS・センサーによる自律航行', 'AIの誘導を継続的に受信'], ['到着前の顧客通知'], ['指定受取地点に配送'], ['運用記録を保存し', 'その後のAI改善に利用']] if ja else
              [['Receive delivery request'], ['Determine destination', 'Assign drone and plan route'], ['Navigate with GPS and sensors', 'Receive ongoing AI guidance'], ['Notify customer before arrival'], ['Deliver at designated point'], ['Retain operational records', 'Use data for AI improvement']])
    s = ''
    for i, value in enumerate(values):
        y = 95 + i * 134
        s += block(290, y, 540, 104, f'S{(i + 1) * 10}', value, 22)
        if i < 5:
            s += line(f'M560 {y + 104} V{y + 134}', arrow=True)
    s += line('M830 550 H875')
    s += lines(886, 541, ['到着の', '約5分前'] if ja else ['Approx. 5 min', 'before arrival'], 18, 26, anchor='start')
    notes = (['S10〜S60は、本資料で配送手順を参照するための整理番号です。', '通知時刻は原文の目標値であり、実測した配送時間ではありません。'] if ja else
             ['S10–S60 identify the source delivery steps for this portfolio.', 'The notification interval is a source target; no measured delivery duration is implied.'])
    sheet('delivery-sequence', 3, '配送手順' if ja else 'Delivery procedure', s, 1065, lang, notes)


def drone(lang):
    ja = lang == 'ja'
    s = block(360, 100, 400, 100, '120 / 130', ['中央AI制御・衛星通信' if ja else 'AI control / satellite link'])
    s += rect(110, 270, 900, 540)
    s += text(155, 311, '140  自律型ドローン' if ja else '140  Autonomous drone', 24, 'start')
    s += line('M560 200 V345', both=True)
    s += block(355, 345, 410, 100, '144', ['通信モジュール' if ja else 'Communication modules'])
    for x, ref, label in [(150, '141', ['GPS測位'] if ja else ['GPS positioning']),
                           (445, '142', ['物体検知センサー'] if ja else ['Object-detection', 'sensors']),
                           (740, '143', ['カメラ'] if ja else ['Cameras'])]:
        s += block(x, 510, 230, 110, ref, label, 20)
    s += block(355, 680, 410, 90, '145', ['電動推進' if ja else 'Electric propulsion'])
    notes = (['構成要素を機能別に整理した図です。配置、寸法、配線、制御実装は示していません。', 'GPSは測位、衛星通信は情報交換のための別の機能として表しています。'] if ja else
             ['Functional component inventory. Placement, dimensions, wiring, and control implementation are unspecified.',
              'GPS supplies positioning; satellite communication provides a separate information-exchange function.'])
    sheet('drone-components', 4, 'ドローンの機能構成' if ja else 'Drone functional components', s, 1030, lang, notes)


def safety(lang):
    ja = lang == 'ja'
    s = rect(100, 110, 920, 75) + text(560, 157, '継続的な監視・通信経路の冗長化' if ja else 'Continuous monitoring / redundant communication links', 24)
    s += line('M560 185 V240 M215 240 H905 M215 240 V310 M560 240 V310 M905 240 V310')
    branches = ([(['障害物を検知'], ['飛行経路を', '自動調整'], ['対象：人・車両など', '近傍の障害物']),
                  (['通信の喪失'], ['基地への帰還', 'または安全な着陸'], ['通信復旧・動作選択の', '条件は実装時に定義']),
                  (['電源の異常'], ['基地への帰還', 'または安全な着陸'], ['動作の実現可能性は', '残存電力・機体状態による'])] if ja else
                [(['Obstacle detected'], ['Adjust flight path', 'to avoid obstacle'], ['Examples: nearby', 'people or vehicles']),
                 (['Communication loss'], ['Return to base', 'or land safely'], ['Recovery and response', 'criteria require definition']),
                 (['Power failure'], ['Return to base', 'or land safely'], ['Feasibility depends on', 'power and aircraft state'])])
    for x, ref, (trigger, response, note) in zip([75, 420, 765], ['A', 'B', 'C'], branches):
        s += block(x, 310, 280, 100, ref, trigger, 21)
        s += line(f'M{x+140} 410 V490', arrow=True)
        s += rect(x, 490, 280, 120) + lines(x + 140, 538, response, 22)
        s += lines(x + 140, 662, note, 18, 27)
    notes = (['A〜Cは原文の異常シナリオを並列に整理したものです。優先順位は示していません。', '帰還・着陸は記載された目標動作です。完全な電力喪失時の実現を保証するものではありません。'] if ja else
             ['A–C are separate source scenarios; no priority or response-selection policy is specified.',
              'Return and landing are intended responses; feasibility after total loss of power is not established.'])
    sheet('safety-responses', 5, '異常時の応答' if ja else 'Safety response scenarios', s, 940, lang, notes)


def learning(lang):
    ja = lang == 'ja'
    s = text(300, 122, '明細書に記載された流れ' if ja else 'Flow described in the specification', 22)
    source = [('140', ['飛行経路・センサー値・画像'] if ja else ['Flight paths / readings / images']),
              ('150', ['暗号化クラウドDBに保存'] if ja else ['Encrypted cloud storage']),
              ('160', ['AIによる処理と学習'] if ja else ['AI processing and learning']),
              ('160', ['航行・エネルギー効率・', '物流計画の改善'] if ja else ['Improve navigation, energy use,', 'and logistics planning'])]
    for i, (ref, label) in enumerate(source):
        y = 175 + 160 * i
        s += block(85, y, 430, 110, ref, label, 21)
        if i < 3:
            s += line(f'M300 {y+110} V{y+160}', arrow=True)
    s += rect(610, 95, 425, 720, dashed=True)
    s += text(822, 140, '実装上の提案' if ja else 'Proposed implementation controls', 21)
    proposed = ([['データ品質の検証'], ['候補モデルの評価'], ['更新の承認とバージョン管理'], ['運用監視・ロールバック']] if ja else
                [['Validate data quality'], ['Evaluate candidate models'], ['Approve and version releases'], ['Monitor / support rollback']])
    for i, label in enumerate(proposed):
        y = 200 + 155 * i
        s += rect(647, y, 350, 90) + lines(822, y + 54, label, 20)
        if i < 3:
            s += line(f'M822 {y+90} V{y+155}', arrow=True)
    notes = (['破線内はシステム設計上の提案であり、明細書の記載事項ではありません。', '原文はモデル配置、学習スケジュール、更新の承認方法を指定していません。'] if ja else
             ['The dashed enclosure contains portfolio engineering proposals beyond the supplied specification.',
              'Model placement, training schedules, and release approval are not defined in the source.'])
    sheet('learning-flow', 6, '運用データとAIの改善' if ja else 'Operational data and AI improvement', s, 1030, lang, notes)


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for language in ('en', 'ja'):
        for draw in (architecture, coordination, delivery, drone, safety, learning):
            draw(language)
    print('Built 12 explanatory SVG drawing sheets.')
