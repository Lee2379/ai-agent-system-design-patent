"""Build bilingual, source-aligned SVG illustrations with Python's standard library."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
NAVY, INK, MUTED = '#10283f', '#17344d', '#536d81'
TEAL, BLUE, GOLD = '#087f83', '#4668c8', '#ac6b17'
PALE, BORDER = '#f4f7fa', '#d5e1e8'
FONT = "'Segoe UI', 'Yu Gothic', Meiryo, sans-serif"

def tx(x, y, value, size=20, color=INK, weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'

def rect(x, y, w, h, fill='white', stroke=BORDER, radius=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'

def path(d, color=TEAL, width=2.5, dashed=False, arrow=False):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"'+(' stroke-dasharray="7 7"' if dashed else '')+(f' marker-end="url(#{color[1:]})"' if arrow else '')+'/>'

def circle(x,y,r,fill,stroke='none'):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}"/>'

def textlines(x,y,lines,size=19,color=MUTED,step=29):
    return ''.join(tx(x,y+i*step,v,size,color) for i,v in enumerate(lines))

def icon(kind, x, y, scale=1, color=TEAL):
    shapes={
      'drone':'<path d="M-26 -18 L26 18 M-26 18 L26 -18"/><rect x="-12" y="-9" width="24" height="18" rx="5"/><ellipse cx="-29" cy="-20" rx="18" ry="6"/><ellipse cx="29" cy="-20" rx="18" ry="6"/><ellipse cx="-29" cy="20" rx="18" ry="6"/><ellipse cx="29" cy="20" rx="18" ry="6"/><path d="M-7 11 V28 H7 V11"/>',
      'warehouse':'<path d="M-40 4 L0 -24 L40 4 V48 H-40 Z M-17 48 V10 H17 V48 M-40 0 H40"/>',
      'home':'<path d="M-25 0 L0 -24 L25 0 V32 H-25 Z M-7 32 V10 H7 V32"/>',
      'city':'<path d="M-38 36 V-8 H-10 V36 M-10 36 V-38 H24 V36 M24 36 V3 H43 V36 M-28 3 H-20 M-28 16 H-20 M1 -24 H12 M1 -10 H12 M1 4 H12 M1 18 H12 M-44 36 H49"/>',
      'satellite':'<rect x="-10" y="-12" width="20" height="24" rx="3"/><path d="M-10 -8 H-42 V8 H-10 M10 -8 H42 V8 H10 M-28 -8 V8 M28 -8 V8 M0 12 V27 M-13 18 Q0 39 13 18"/>',
      'database':'<ellipse cx="0" cy="-20" rx="27" ry="9"/><path d="M-27 -20 V25 C-27 38 27 38 27 25 V-20 M-27 -4 C-27 9 27 9 27 -4 M-27 11 C-27 24 27 24 27 11"/>',
      'shield':'<path d="M0 -32 L28 -20 V3 Q28 23 0 38 Q-28 23 -28 3 V-20 Z M-13 0 L-3 11 L15 -9"/>',
      'signal':'<path d="M-30 -12 Q0 -40 30 -12 M-20 0 Q0 -20 20 0 M-10 12 Q0 1 10 12"/><circle cx="0" cy="25" r="3"/>',
      'battery':'<rect x="-32" y="-18" width="58" height="36" rx="5"/><path d="M27 -8 H34 V8 H27 M-23 -10 V10 M-17 -10 V10"/>',
      'obstacle':'<path d="M0 -31 L34 28 H-34 Z M0 -10 V8 M0 17 V19"/>',
      'model':'<circle cx="0" cy="0" r="9"/><circle cx="-28" cy="-22" r="6"/><circle cx="28" cy="-22" r="6"/><circle cx="-28" cy="24" r="6"/><circle cx="28" cy="24" r="6"/><path d="M-8 -6 L-22 -17 M8 -6 L22 -17 M-8 6 L-22 19 M8 6 L22 19"/>',
      'check':'<rect x="-25" y="-30" width="50" height="60" rx="5"/><path d="M-13 -10 L-6 -3 L7 -17 M-12 11 H13 M-12 20 H5"/>',
    }
    return f'<g transform="translate({x} {y}) scale({scale})" stroke="{color}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>'

def base(h, eyebrow, title, subtitle, ja):
    definitions=''.join(f'<marker id="{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{c}"/></marker>' for c in [TEAL,BLUE,GOLD,MUTED])
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{h}" viewBox="0 0 1280 {h}" role="img" aria-labelledby="title desc" lang="'+('ja' if ja else 'en')+f'"><title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc><defs>{definitions}</defs>'+rect(1,1,1278,h-2,PALE,BORDER,20)+tx(40,43,eyebrow,15,TEAL,700)+tx(40,88,title,32,INK,700)+tx(40,123,subtitle,18,MUTED)

def save(stem,ja,s):
    (OUT/f'{stem}-{"ja" if ja else "en"}.svg').write_text(s+'</svg>',encoding='utf-8',newline='\n')

def context(ja):
    s=base(760,'01 / APPLICATION CONTEXT', '都市・山間部・農村部をつなぐ自律配送' if ja else 'One delivery system. Different operating environments.', '顧客の注文、AIによる調整、自律航行、指定地点での受け取りを一つの流れに。' if ja else 'Connect customer requests, AI coordination, autonomous navigation, and a designated handoff.',ja)
    s+=rect(32,153,1216,390,'#edf4f7',BORDER,16)
    # Terrain is illustrative, with no real coordinates or service coverage claims.
    s+='<path d="M34 481 L235 378 L349 440 L540 261 L670 402 L770 336 L940 486 V541 H34Z" fill="#d9e6e9"/><path d="M349 440 L540 261 L595 354 L553 338 L533 369 L509 341Z" fill="#f9fcfd"/><path d="M35 504 Q256 462 421 495 T778 492 T1246 510 V542 H35Z" fill="#cddfdc"/>'
    s+=path('M54 519 Q278 482 443 512 T780 517 T1230 520','#b0c9c9',3)
    s+=icon('warehouse',142,412,1.1,NAVY)+icon('city',1087,327,1.22,NAVY)+icon('home',1033,451,.88,NAVY)+icon('home',1125,465,.75,NAVY)
    s+=path('M180 410 C345 270 717 173 1036 301',TEAL,3,True,True)
    s+=path('M719 272 Q899 344 990 435',TEAL,3,True,True)
    s+=icon('drone',681,265,1.16,TEAL)+icon('satellite',394,208,.76,BLUE)
    s+=tx(337,181,'衛星通信' if ja else 'Satellite link',16,BLUE,600)
    s+=tx(620,325,'GPS・センサー' if ja else 'GPS + sensors',16,TEAL,600)
    s+=path('M415 233 Q502 247 624 261',BLUE,2,True)
    s+=rect(58,179,228,96,'white',BORDER,12)+tx(76,211,'AI制御サーバー' if ja else 'AI control server',20,INK,650)+tx(76,242,'計画・通信・調整' if ja else 'Plan · connect · coordinate',16,MUTED)
    s+=path('M174 276 V350',BLUE,2,True)
    s+=rect(879,179,323,91,'white',BORDER,12)+tx(897,212,'到着前通知' if ja else 'Pre-arrival notification',21,INK,650)+tx(897,243,'到着の約5分前に顧客へ' if ja else 'Customer alert ~5 min before arrival',16,MUTED)
    s+=tx(66,499,'配送拠点' if ja else 'Dispatch base',18,INK,650)
    s+=tx(493,461,'地形に応じた経路計画' if ja else 'Terrain-aware routing',18,MUTED)
    s+=tx(1019,398,'指定受取地点' if ja else 'Delivery points',18,INK,650)
    labels=[('都市部','配送地点と周囲の障害物を考慮'),('山間部','地形と環境の変化に応じて調整'),('農村部','分散した配送先へのアクセス')] if ja else [('Urban areas','Defined handoff points and obstacles'),('Mountainous areas','Routes shaped by terrain and conditions'),('Rural communities','Access to dispersed destinations')]
    for i,(title,body) in enumerate(labels):
        x=32+i*411
        s+=rect(x,565,394,116)+tx(x+20,600,f'0{i+1}',16,TEAL,700)+tx(x+63,600,title,22,INK,650)+tx(x+20,636,body,17,MUTED)
    s+=tx(40,722,'明細書に基づく概念図。地理的な配置と飛行経路は説明用です。',16,MUTED) if ja else tx(40,722,'Concept illustration based on the specification. Geography and flight paths are illustrative.',16,MUTED)
    save('delivery-context',ja,s)

def coordination(ja):
    s=base(864,'03 / AGENT COORDINATION','役割を分け、判断と情報をつなぐ' if ja else 'Separate responsibilities. Connected decisions.', '配送依頼から経路の更新、到着通知までの概念的な情報の流れ。' if ja else 'A conceptual interaction between the customer, fleet coordination, network agents, and drone.',ja)
    centers=[185,490,795,1100]
    names=['顧客プラットフォーム','階層型AI','ネットワーク型AI','自律型ドローン'] if ja else ['Customer platform','Hierarchical AI','Network AI','Autonomous drone']
    descs=['依頼・受け取り','割当・経路の判断','通信・情報の共有','飛行・周囲の検知'] if ja else ['Request and receive','Assign and route','Exchange and coordinate','Navigate and sense']
    colors=[MUTED,BLUE,TEAL,GOLD]
    for x,n,d,c in zip(centers,names,descs,colors):
        s+=rect(x-136,157,272,88,'white',BORDER,12)+tx(x,191,n,21,c,650,'middle')+tx(x,223,d,16,MUTED,400,'middle')
        s+=path(f'M{x} 248 V695','#c6d4dd',1.5,True)
    rows=[(0,1,'配送依頼と目的地' if ja else 'Request + destination',BLUE),(1,2,'機体割当と経路' if ja else 'Assignment + route',BLUE),(2,3,'ミッション情報' if ja else 'Mission information',TEAL),(3,2,'位置・状態の報告' if ja else 'Position + status',GOLD),(2,1,'調整用の情報' if ja else 'Coordination data',TEAL),(1,3,'ネットワーク型AIを介した誘導更新' if ja else 'Guidance update through network agents',BLUE),(2,0,'到着前通知（約5分前）' if ja else 'Pre-arrival alert (~5 min)',TEAL)]
    for i,(a,b,label,c) in enumerate(rows):
        y=290+i*61
        x1,x2=centers[a],centers[b]
        s+=circle(x1,y,4,c)+path(f'M{x1} {y} H{x2}',c,2.5,False,True)
        cx=(x1+x2)/2
        # Put an opaque backing under each label so lane guides never run through text.
        width=(len(label)*10 if not ja else len(label)*18)+24
        s+=rect(cx-width/2,y-34,width,27,PALE,PALE,4)+tx(cx,y-13,label,17,INK,500,'middle')
    s+=rect(49,724,1182,73,'#e7f3f2','#bfdcd8',12)+tx(71,755,'判断 → 共有 → 実行 → フィードバック' if ja else 'Decide → share → execute → report back',22,TEAL,650)+tx(71,782,'通信方式やエージェントの物理的配置は、実装時に定義します。' if ja else 'The specification leaves protocols and the physical placement of agents to implementation.',16,MUTED)
    s+=tx(40,837,'説明用のシーケンス。実機で測定した通信履歴ではありません。' if ja else 'Illustrative sequence derived from the specification; no measured flight or communication trace is implied.',16,MUTED)
    save('agent-coordination',ja,s)

def safety(ja):
    s=base(734,'05 / SAFETY RESPONSES','環境の変化を検知し、状況に応じて対応する' if ja else 'Detect the change. Select an appropriate response.', '明細書に記載された安全動作と、実装時に定義する条件を対応付けます。' if ja else 'Connect safety behavior described in the specification with conditions to define during implementation.',ja)
    headers=['検知する状況','原文に記載された動作','実装時に定義する条件'] if ja else ['DETECTED CONDITION','RESPONSE IN THE SOURCE','IMPLEMENTATION CONDITIONS']
    for x,h in zip([56,454,880],headers):s+=tx(x,182,h,15,MUTED,700)
    rows=[('obstacle','障害物を検知',['経路を調整','衝突を回避'],['検知距離・回避性能','センサー状態']) ,('signal','通信が途絶',['通信経路の冗長化','帰還または安全な着陸'],['タイムアウト・代替動作','機体側の判断権限']),('battery','電源に異常',['帰還または安全な着陸','実行可能な条件で対応'],['残量の閾値・着陸可能性','完全な電源喪失は別途扱う'])] if ja else [('obstacle','Obstacle detected',['Adjust the flight path','Avoid a collision'],['Detection and avoidance limits','Sensor-health criteria']),('signal','Communication lost',['Redundant communication','Return to base or land safely'],['Timeout and fallback policy','Onboard decision authority']),('battery','Power problem',['Return to base or land safely','Where controlled flight is feasible'],['Energy threshold and landing feasibility','Total power loss needs separate handling'])]
    for i,(sym,label,response,conditions) in enumerate(rows):
        y=205+i*145
        s+=rect(32,y,1216,126)+circle(93,y+60,38,'#eef3f7')+icon(sym,93,y+58,.69,GOLD)
        s+=tx(149,y+67,label,22,INK,650)+path(f'M381 {y+63} H424',TEAL,2.5,False,True)
        s+=textlines(454,y+50,response,19,INK)+path(f'M847 {y+22} V{y+104}',BORDER,1.5)
        s+=textlines(880,y+50,conditions,16,MUTED)
    s+=rect(32,658,1216,46,'#fbf2e3','#ead8b6',10)+tx(53,687,'応答の選択条件は未指定です。性能保証や飛行安全性の認証を示す図ではありません。' if ja else 'Trigger thresholds are unspecified. These are design responses, without a flight-safety validation claim.',17,GOLD)
    save('safety-responses',ja,s)

def learning(ja):
    s=base(727,'06 / OPERATIONAL LEARNING','配送データを、次の改善につなげる' if ja else 'Turn delivery records into a controlled improvement cycle.', '原文のデータ活用と、実装に向けて提案する評価・更新の手順。' if ja else 'Distinguish the specified use of operational data from a proposed evaluation and release process.',ja)
    s+=rect(32,158,1216,221,'#e9f4f2','#bfdcd8',15)+tx(53,190,'原文の設計' if ja else 'DESCRIBED IN THE SPECIFICATION',15,TEAL,700)
    xs=[57,464,871]
    data=[('drone','データの収集',['飛行経路・画像','センサー値']),('database','暗号化して保存',['クラウドデータベース','運用記録を蓄積']),('model','AIの改善に利用',['航行・エネルギー効率','物流計画'])] if ja else [('drone','Collect',['Flight paths and images','Sensor readings']),('database','Store',['Encrypted cloud database','Retained operational records']),('model','Improve',['Navigation and energy efficiency','Logistics planning'])]
    for x,(sym,title,lines) in zip(xs,data):
        s+=rect(x,209,351,143)+icon(sym,x+49,257,.63,TEAL)+tx(x+91,253,title,23,INK,650)+textlines(x+22,296,lines,17,MUTED,27)
        if x!=871:s+=path(f'M{x+355} 282 H{x+396}',TEAL,2.5,False,True)
    s+=tx(53,426,'実装上の提案' if ja else 'PROPOSED IMPLEMENTATION PROCESS',15,BLUE,700)
    stages=[('品質確認',['時刻・欠損・出所']),('モデル評価',['シナリオ別に比較']),('更新の承認',['版管理・切り戻し']),('運用監視',['動作の変化を確認'])] if ja else [('Validate data',['Time, gaps, provenance']),('Evaluate model',['Compare across scenarios']),('Approve release',['Version and rollback']),('Monitor',['Review behavior changes'])]
    for i,(label,lines) in enumerate(stages):
        x=32+i*311
        s+=rect(x,451,283,114,'white','#ccd7ed',12)+tx(x+20,484,f'0{i+1}',15,BLUE,700)+tx(x+20,517,label,22,INK,650)+tx(x+20,545,lines[0],15,MUTED)
        if i<3:s+=path(f'M{x+287} 508 H{x+304}',BLUE,2,True,True)
    s+=path('M1180 565 V608 H156 V575',BLUE,2,True,True)+rect(407,589,447,37,PALE,PALE,4)+tx(630,614,'運用結果から次の評価へ' if ja else 'Operational results inform the next review',18,BLUE,500,'middle')
    s+=tx(40,676,'継続的な学習は原文に記載。モデルの更新時期と展開方法は未指定です。' if ja else 'The source describes continuous learning; it does not specify model-update timing or deployment procedures.',16,MUTED)
    save('learning-cycle',ja,s)

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for ja in (False,True):
        context(ja);coordination(ja);safety(ja);learning(ja)
    print('Generated eight bilingual SVG illustrations.')
