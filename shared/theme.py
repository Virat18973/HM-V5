"""
One dark theme and one font pair for the whole app (sinter, MBF and combined pages).

The palette is sampled from the "Hot metal cost planner" prototype screenshot.  The two fonts are the nearest Google
fonts to what the screenshot shows (a bold condensed face for titles and numbers, a humanist sans for text); they are a
best guess until the prototype HTML is available, so they are named once, here (FONT_HEAD, FONT_BODY).
The host needs internet access for Google Fonts; every font has a system fallback.
"""

FONT_HEAD = "Barlow Condensed"
FONT_BODY = "Source Sans 3"

PALETTE = {
    "bg": "#0E1419", "side": "#0A0F13", "card": "#161E25", "active": "#282C30", "line": "#26323C",
    "text": "#E6ECF0", "muted": "#9AA9B5", "dim": "#7B8A96",
    "sinter": "#35B8AA", "furnace": "#8CA4F0", "hm": "#E0A24A",
    "grey1": "#5F8797", "grey2": "#8796A3", "grey3": "#C9D4DC", "flux": "#86A867",
    "short_bg": "#421E19", "short_fg": "#F5B4AB", "ok_bg": "#16382A", "ok_fg": "#A9E3B9",
    "check_bg": "#3A2C12", "check_fg": "#F2CE8E",
}
MODEL_COLOR = {"sinter": PALETTE["sinter"], "mbf": PALETTE["furnace"], "combined": PALETTE["hm"]}

# Old colours of the two original dashboards -> the shared palette.  Applied in memory to the colour strings the
# original page code uses (chart series, inline HTML); the files on disk are not changed.
COLOR_MAP = {
    "#22304C": "#26323C", "#4C8DFF": "#8CA4F0", "#F5A85C": "#E0A24A", "#3FD6A8": "#5CC48E", "#3FD6B0": "#35B8AA",
    "#5B6B8C": "#5F8797", "#7C8CAD": "#8796A3", "#94A2C2": "#C9D4DC", "#8B9BC0": "#9AA9B5", "#A78BFA": "#86A867",
    "#FF6B6B": "#E5675D", "#0B1220": "#0E1419", "#1F5A44": "#2A5A44", "#7A2F33": "#6E2E28", "#FACC15": "#F2CE8E",
    "#F472B6": "#D98BB0", "#1F9C7F": "#2A8F82", "#EAF0FB": "#E6ECF0", "#6B5620": "#6B5420", "#8DB6FF": "#A9BDF5",
    "#2E5FB8": "#5C77C9", "#BFD6FF": "#C9D4F5", "#8CEBD2": "#8FDACF", "#C4B5FD": "#CDB9EF", "#FFD29E": "#F2D3A1",
    "#8391B0": "#8796A3", "#3E4A63": "#3F4E5A", "#B8C3DB": "#C9D4DC", "#08101F": "#0A0F13", "#F0B94E": "#E0A24A",
    "#3C4250": "#3F4A54", "#FF8B6B": "#E8836F", "#16213A": "#161E25", "#111A2E": "#161E25",
}
FONT_MAP = {"Manrope": FONT_BODY}


def restyle_string(s):
    """Map the old colours / font names inside one string of the original page code."""
    if "#" in s:
        import re
        s = re.sub(r"#[0-9A-Fa-f]{6}\b", lambda m: COLOR_MAP.get(m.group(0).upper(), m.group(0)), s)
    for old, new in FONT_MAP.items():
        if old in s:
            s = s.replace(old, new)
    return s


def css(model="combined", compact=False):
    p = PALETTE
    accent = MODEL_COLOR.get(model, p["hm"])
    sw, pad = (80, 0.55) if compact else (272, 0.9)
    rail_css = '[data-testid="stSidebar"] button { justify-content:center; padding:.1rem 0; }\n[data-testid="stSidebar"] button > div { justify-content:center; }\n[data-testid="stSidebar"] [data-testid="stHorizontalBlock"] { flex-direction:column; align-items:center; gap:.4rem; }\n[data-testid="stSidebar"] .brand-row { justify-content:center; }' if compact else ""
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family={FONT_HEAD.replace(' ', '+')}:wght@500;600;700;800&family={FONT_BODY.replace(' ', '+')}:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap');
.material-symbols-outlined {{ font-family:'Material Symbols Outlined'; font-weight:normal; font-style:normal; font-size:20px; line-height:1;
  letter-spacing:normal; text-transform:none; white-space:nowrap; direction:ltr; -webkit-font-smoothing:antialiased; vertical-align:middle; }}
:root {{ --bg:{p['bg']}; --side:{p['side']}; --card:{p['card']}; --panel:{p['card']}; --panel2:{p['card']}; --active:{p['active']};
  --line:{p['line']}; --text:{p['text']}; --muted:{p['muted']}; --dim:{p['dim']}; --accent:{accent};
  --sinter:{p['sinter']}; --furnace:{p['furnace']}; --hm:{p['hm']}; --good:#5CC48E; --warn:{p['hm']}; --bad:#E5675D;
  --head:'{FONT_HEAD}','Arial Narrow','Roboto Condensed',sans-serif; --body:'{FONT_BODY}','Segoe UI',system-ui,sans-serif; }}

html, body, .stApp, [data-testid="stAppViewContainer"] {{ background:var(--bg); color:var(--text); font-family:var(--body); font-feature-settings:'tnum' 1,'lnum' 1; }}
[data-testid="stHeader"] {{ background:transparent; }}
[data-testid="stMainBlockContainer"], .block-container {{ max-width:1500px; padding:1.3rem 1.8rem 3rem; }}
h1, h2, h3, h4 {{ font-family:var(--head) !important; font-weight:700 !important; letter-spacing:.005em !important; color:var(--text); }}
h1 {{ font-size:2.1rem !important; margin:0 0 .1rem !important; padding:0 !important; }}
h2 {{ font-size:1.6rem !important; }} h3 {{ font-size:1.3rem !important; }}
p, label, span, li {{ font-family:var(--body); }}
.sub {{ color:var(--muted); font-size:.98rem; margin:0 0 1.1rem; max-width:80ch; }}
.small {{ color:var(--muted); font-size:.82rem; }}
.eyebrow {{ color:var(--accent); font-size:.72rem; letter-spacing:.16em; font-weight:700; text-transform:uppercase; }}

/* sidebar: brand, search, collapsible model sections with pill items, compact icon rail */
[data-testid="stSidebar"] {{ background:var(--side); border-right:1px solid var(--line); min-width:{sw}px !important; max-width:{sw}px !important; }}
[data-testid="stSidebar"] > div:first-child {{ width:{sw}px !important; }}
[data-testid="stSidebarContent"] {{ padding:0 {pad}rem; }}
[data-testid="stSidebarHeader"] {{ display:none; }}
[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {{ padding:1.1rem 0 1rem; }}
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label, [data-testid="stSidebar"] div {{ color:var(--text); }}
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{ gap:.3rem; }}
[data-testid="stSidebar"] .brand-row {{ display:flex; align-items:center; gap:.65rem; padding:.1rem .35rem; }}
[data-testid="stSidebar"] .brand-mark {{ width:24px; height:24px; flex:none; background:var(--accent); border-radius:8px 8px 8px 2px; display:inline-block; }}
[data-testid="stSidebar"] .brand {{ font-family:var(--head); font-size:1.5rem; font-weight:700; line-height:1.05; }}
[data-testid="stSidebar"] .brand-sub {{ font-size:.78rem; color:var(--muted); margin:.3rem .35rem .6rem; line-height:1.35; }}
[data-testid="stSidebar"] .nav-group {{ font-size:.68rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--dim); margin:.7rem 0 .15rem .6rem; }}
[data-testid="stSidebar"] .rail-sep {{ height:1px; background:var(--line); margin:.5rem .4rem; }}
[data-testid="stSidebar"] .side-foot {{ font-size:.8rem; color:var(--muted); line-height:1.55; margin-top:1rem; border:1px solid var(--line); background:var(--card); border-radius:14px; padding:.8rem .95rem; }}
[data-testid="stSidebar"] .side-foot b {{ color:var(--text); font-weight:600; }}
/* search */
[data-testid="stSidebar"] [data-testid="stTextInput"] > div {{ background:var(--card); border:1px solid var(--line); border-radius:999px; min-height:2.5rem; }}
[data-testid="stSidebar"] [data-testid="stTextInput"] input {{ background:transparent; font-size:.92rem; }}
[data-testid="stSidebar"] [data-testid="stTextInput"] > div:focus-within {{ border-color:var(--muted); }}
/* model sections */
[data-testid="stSidebar"] [data-testid="stExpander"] {{ border:none; background:transparent; }}
[data-testid="stSidebar"] [data-testid="stExpander"] details {{ border:none; background:transparent; }}
[data-testid="stSidebar"] [data-testid="stExpander"] summary {{ padding:.55rem .6rem; border-radius:999px; font-weight:600; font-size:.95rem; }}
[data-testid="stSidebar"] [data-testid="stExpander"] summary:hover {{ background:var(--card); }}
[data-testid="stSidebar"] [data-testid="stExpander"] summary p {{ font-weight:600; }}
[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] {{ padding:.05rem 0 .35rem .15rem; }}
/* items: rounded pills, icon then label */
[data-testid="stSidebar"] button {{ justify-content:flex-start; text-align:left; border-radius:999px; min-height:2.5rem; padding:.1rem .95rem; font-size:.93rem; gap:.65rem; }}
[data-testid="stSidebar"] button[kind="secondary"], [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {{ background:transparent !important; border:1px solid transparent !important; color:var(--muted) !important; }}
[data-testid="stSidebar"] button[kind="secondary"]:hover, [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {{ background:var(--card) !important; color:var(--text) !important; }}
[data-testid="stSidebar"] button[kind="primary"], [data-testid="stSidebar"] [data-testid="stBaseButton-primary"] {{ background:var(--active) !important; border:1px solid #3A4854 !important; color:var(--text) !important; font-weight:600 !important; }}
[data-testid="stSidebar"] button[kind="primary"] p, [data-testid="stSidebar"] [data-testid="stBaseButton-primary"] p {{ color:var(--text) !important; }}
[data-testid="stSidebar"] button[kind="primary"]:hover, [data-testid="stSidebar"] [data-testid="stBaseButton-primary"]:hover {{ background:#30353A !important; }}
[data-testid="stSidebar"] button p {{ color:inherit; text-align:left; width:100%; margin:0; }}
[data-testid="stSidebar"] button > div, [data-testid="stSidebar"] button [data-testid="stMarkdownContainer"] {{ justify-content:flex-start; text-align:left; width:100%; }}
[data-testid="stSidebar"] button span[data-testid="stIconMaterial"], [data-testid="stSidebar"] button [data-testid="stIconMaterial"] {{ font-size:1.25rem; color:inherit; flex:none; }}
{rail_css}

/* cards shared by both original dashboards: flat, thin border, no shadow */
.kpi {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:.75rem .9rem .7rem; min-height:92px; position:relative; }}
.kpi .top {{ display:flex; align-items:flex-start; justify-content:space-between; }}
.kpi .l, .kpi-label {{ color:var(--muted); font-size:.82rem; letter-spacing:.02em; }}
.kpi .ic {{ width:30px; height:30px; border-radius:7px; display:flex; align-items:center; justify-content:center; background:rgba(154,169,181,.12); color:var(--muted); flex:none; }}
.kpi.g .ic {{ background:rgba(92,196,142,.14); color:var(--good); }} .kpi.a .ic {{ background:rgba(224,162,74,.16); color:var(--hm); }}
.kpi.r .ic {{ background:rgba(229,103,93,.15); color:var(--bad); }} .kpi.p .ic {{ background:rgba(134,168,103,.16); color:#86A867; }} .kpi.c .ic {{ background:rgba(140,164,240,.15); color:var(--furnace); }}
.kpi .v, .kpi-value {{ font-family:var(--head); font-size:1.85rem; font-weight:700; line-height:1.1; margin-top:.3rem; }}
.kpi .s, .kpi-sub {{ color:var(--muted); font-size:.8rem; margin-top:.12rem; }}
.kpi .s.trend-up {{ color:var(--good); }} .kpi .s.trend-down {{ color:var(--bad); }}
.kpi-g {{ border-top:3px solid var(--good); }} .kpi-r {{ border-top:3px solid var(--bad); }} .kpi-a {{ border-top:3px solid var(--hm); }} .kpi-s {{ border-top:3px solid var(--accent); }}
.panel, .hero {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:.7rem .85rem; margin:.5rem 0; }}
.panel-title {{ font-family:var(--head); font-size:1.15rem; font-weight:700; letter-spacing:.02em; margin:.2rem 0 .35rem; color:var(--text); text-transform:none; }}
.panel-note {{ color:var(--muted); font-size:.86rem; margin:-.1rem 0 .5rem; }}
.notice {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:.6rem .85rem; font-size:.93rem; margin:.3rem 0 .8rem; color:var(--text); }}
.notice b {{ font-weight:700; }}
.notice.w, .notice-w {{ border-color:#5A4518; background:{p['check_bg']}; color:{p['check_fg']}; }}
.notice.r, .notice-r {{ border-color:#6E2E28; background:{p['short_bg']}; color:{p['short_fg']}; }}
.notice.g {{ border-color:#2A5A44; background:{p['ok_bg']}; color:{p['ok_fg']}; }}
.pill {{ display:inline-block; border-radius:999px; padding:.15rem .75rem; font-size:.85rem; font-weight:700; border:1px solid var(--line); background:var(--card); }}
.pill.g {{ color:{p['ok_fg']}; border-color:#2A5A44; background:{p['ok_bg']}; }} .pill.a {{ color:{p['check_fg']}; border-color:#5A4518; background:{p['check_bg']}; }}
.pill.r {{ color:{p['short_fg']}; border-color:#6E2E28; background:{p['short_bg']}; }}
.vsline {{ color:var(--muted); font-size:.88rem; margin-left:.8rem; }}
.note-line {{ font-size:.92rem; padding:.4rem .7rem; border-radius:6px; margin:.28rem 0; background:var(--card); border-left:3px solid var(--line); }}
.note-line.chk {{ border-left-color:var(--hm); }} .note-line.wrn {{ border-left-color:var(--bad); }} .note-line.nt {{ border-left-color:var(--furnace); }}
.bandrow {{ display:grid; grid-template-columns:150px 1fr 74px; gap:.7rem; align-items:center; margin:.42rem 0 .12rem; }}
.bandlabel {{ font-size:.93rem; }}
.bandtrack {{ position:relative; height:12px; background:{p['side']}; border-radius:6px; border:1px solid var(--line); }}
.bandzone {{ position:absolute; top:-1px; bottom:-1px; background:rgba(140,164,240,.20); border:1px solid rgba(140,164,240,.5); border-radius:6px; }}
.bandmark {{ position:absolute; top:-5px; width:6px; height:20px; border-radius:3px; background:var(--good); transform:translateX(-3px); box-shadow:0 0 0 2px var(--bg); }}
.bandmark.a {{ background:var(--hm); }} .bandmark.r {{ background:var(--bad); }}
.bandval {{ text-align:right; font-weight:700; font-size:.98rem; }} .bandval.a {{ color:var(--hm); }} .bandval.r {{ color:var(--bad); }}
.bandrange {{ grid-column:2 / 4; color:var(--muted); font-size:.78rem; margin:-.05rem 0 .2rem; }}
.footer, .foot {{ color:var(--dim); font-size:.8rem; text-align:right; margin-top:1.6rem; }}

/* widgets */
div.stButton > button, div.stDownloadButton > button {{ border-radius:7px; font-weight:600; background:var(--card); border:1px solid #33414D; color:var(--text); }}
div.stButton > button:hover, div.stDownloadButton > button:hover {{ border-color:var(--muted); color:#fff; }}
button[kind="primary"], [data-testid="stBaseButton-primary"] {{ background:var(--text) !important; border-color:var(--text) !important; color:{p['bg']} !important; font-weight:700 !important; }}
button[kind="primary"] p, [data-testid="stBaseButton-primary"] p {{ color:{p['bg']} !important; }}
button[kind="primary"]:hover, [data-testid="stBaseButton-primary"]:hover {{ background:#fff !important; }}
[data-testid="stTabs"] [data-baseweb="tab-list"] {{ gap:.2rem; border-bottom:1px solid var(--line); }}
[data-testid="stTabs"] [data-baseweb="tab"] {{ font-size:.97rem; font-weight:500; color:var(--muted); padding:.5rem .95rem; background:transparent; }}
[data-testid="stTabs"] [aria-selected="true"] {{ color:var(--text); }}
[data-testid="stTabs"] [data-baseweb="tab-highlight"] {{ background:var(--accent) !important; }}
[data-testid="stDataFrame"], [data-testid="stDataEditor"] {{ border:1px solid var(--line); border-radius:8px; overflow:hidden; }}
[data-testid="stExpander"] {{ border:1px solid var(--line); border-radius:8px; background:var(--card); }}
[data-testid="stFileUploader"] section {{ background:var(--card); border:1px dashed #33414D; border-radius:8px; }}
[data-testid="stMetric"] {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:.5rem .7rem; }}

/* combined page */
.hdr-title {{ font-family:var(--head); font-size:2.3rem; font-weight:700; line-height:1.05; }}
.stage {{ background:var(--card); border:1px solid var(--line); border-top:3px solid var(--c, var(--muted)); border-radius:6px; padding:.85rem 1rem .9rem; min-height:150px; }}
.stage .nm {{ color:var(--c); font-weight:600; font-size:.95rem; }}
.stage .big {{ font-family:var(--head); font-size:2.35rem; font-weight:700; line-height:1.05; margin:.15rem 0 .1rem; }}
.stage .big small {{ font-family:var(--body); font-size:.85rem; font-weight:400; color:var(--muted); margin-left:.3rem; }}
.stage .ln {{ color:var(--muted); font-size:.86rem; line-height:1.55; }}
.stage.hero-hm .big {{ font-size:4.1rem; }}
.arrowcell {{ display:flex; flex-direction:column; align-items:center; justify-content:center; height:150px; color:var(--muted); font-size:.78rem; text-align:center; gap:.3rem; }}
.arrowcell .ar {{ width:74px; height:1px; background:var(--muted); position:relative; }}
.arrowcell .ar:after {{ content:''; position:absolute; right:0; top:-4px; width:8px; height:8px; border-top:1px solid var(--muted); border-right:1px solid var(--muted); transform:rotate(45deg); }}
.mrow {{ display:grid; grid-template-columns:1fr 100px 110px 80px; gap:.5rem; padding:.5rem .3rem; border-bottom:1px solid var(--line); font-size:.95rem; align-items:center; }}
.mrow.hd {{ color:var(--muted); font-size:.78rem; font-weight:700; border-bottom:1px solid #3A4854; }}
.mrow.tot {{ font-weight:700; border-bottom:none; border-top:1px solid #3A4854; }}
.mrow span:not(:first-child) {{ text-align:right; font-variant-numeric:tabular-nums; }}
.sw {{ display:inline-block; width:11px; height:11px; border-radius:2px; margin-right:.55rem; vertical-align:-1px; }}
.propbar {{ display:flex; height:20px; border-radius:3px; overflow:hidden; margin:.4rem 0 .8rem; }}
.alert {{ border-radius:6px; padding:.65rem .85rem; margin:.45rem 0; font-size:.93rem; display:flex; gap:.8rem; align-items:flex-start; }}
.alert b {{ font-size:.82rem; min-width:3.4rem; font-weight:700; }}
.alert.short {{ background:{p['short_bg']}; color:{p['short_fg']}; }} .alert.ok {{ background:{p['ok_bg']}; color:{p['ok_fg']}; }} .alert.check {{ background:{p['check_bg']}; color:{p['check_fg']}; }}
.chip {{ display:inline-block; border-radius:5px; padding:.12rem .55rem; font-size:.78rem; font-weight:700; margin-right:.35rem; border:1px solid var(--line); background:var(--card); color:var(--muted); }}
.chip.ok {{ background:{p['ok_bg']}; color:{p['ok_fg']}; border-color:#2A5A44; }} .chip.check {{ background:{p['check_bg']}; color:{p['check_fg']}; border-color:#5A4518; }}
.chip.short {{ background:{p['short_bg']}; color:{p['short_fg']}; border-color:#6E2E28; }}
.statrow {{ display:flex; gap:2rem; flex-wrap:wrap; color:var(--muted); font-size:.82rem; margin:.4rem 0 .6rem; }}
.statrow b {{ display:block; color:var(--text); font-size:1.02rem; font-weight:600; }}
.sect {{ font-family:var(--head); font-size:1.5rem; font-weight:700; margin:.9rem 0 .15rem; }}
.sect small {{ font-family:var(--body); font-size:.85rem; font-weight:400; color:var(--muted); margin-left:.5rem; }}

/* one layout grid for every page (the originals' pages included): same page width, same gaps, aligned input rows, equal-height cards */
[data-testid="stMainBlockContainer"], .block-container {{ max-width:1440px; padding:1.4rem 2rem 3rem; }}
[data-testid="stMain"] [data-testid="stVerticalBlock"] {{ gap:.75rem; }}
[data-testid="stMain"] [data-testid="stHorizontalBlock"] {{ gap:1rem; }}
[data-testid="stColumn"] {{ min-width:0; }}
[data-testid="stMain"] [data-testid="stHorizontalBlock"]:has([data-testid="stNumberInput"], [data-testid="stSelectbox"], [data-testid="stTextInput"], [data-testid="stDateInput"], [data-testid="stMultiSelect"]) {{ align-items:flex-end; }}
[data-testid="stWidgetLabel"] {{ min-height:1.45rem; margin-bottom:.15rem; align-items:center; }}
[data-testid="stWidgetLabel"] p {{ font-size:.88rem; color:var(--muted); line-height:1.3; }}
[data-testid="stNumberInput"] input, [data-testid="stTextInput"] input {{ min-height:2.5rem; }}
[data-baseweb="select"] > div {{ min-height:2.5rem; }}
div.stButton > button, div.stDownloadButton > button, [data-testid="stFormSubmitButton"] button {{ min-height:2.5rem; }}
[data-testid="stMain"] [data-testid="stColumn"] > [data-testid="stVerticalBlock"] {{ height:100%; }}
[data-testid="stMain"] [data-testid="stElementContainer"]:has(> [data-testid="stMarkdown"] .stage), [data-testid="stMain"] [data-testid="stElementContainer"]:has(> [data-testid="stMarkdown"] .kpi) {{ flex:1; }}
[data-testid="stMarkdown"]:has(> [data-testid="stMarkdownContainer"] > .stage), [data-testid="stMarkdown"]:has(> [data-testid="stMarkdownContainer"] > .kpi) {{ height:100%; }}
[data-testid="stMarkdownContainer"] > .stage, [data-testid="stMarkdownContainer"] > .kpi {{ height:100%; box-sizing:border-box; }}
.sect {{ margin:1.3rem 0 .45rem; padding-bottom:.35rem; border-bottom:1px solid var(--line); }}
.sub {{ margin:0 0 1rem; }}
.notice {{ margin:.2rem 0 .6rem; }}
[data-testid="stExpander"] summary {{ padding:.65rem .9rem; }}
[data-testid="stDataFrame"], [data-testid="stDataEditor"] {{ margin:.1rem 0; }}
</style>
"""


# ------------------------------------------------------------------ small HTML helpers for the combined pages
def stage_card(name, color, big, unit="", lines=(), hero=False):
    ln = "".join(f"<div class='ln'>{x}</div>" for x in lines)
    small = f"<small>{unit}</small>" if unit else ""
    cls = "stage hero-hm" if hero else "stage"
    return f"<div class='{cls}' style='--c:{color}'><div class='nm'>{name}</div><div class='big'>{big}{small}</div>{ln}</div>"


def arrow_cell(label):
    return f"<div class='arrowcell'><div class='ar'></div><div>{label}</div></div>"


def alert(kind, text):
    word = {"short": "Short", "ok": "OK", "check": "Check"}[kind]
    return f"<div class='alert {kind}'><b>{word}</b><span>{text}</span></div>"


def chip(kind, text):
    return f"<span class='chip {kind}'>{text}</span>"
