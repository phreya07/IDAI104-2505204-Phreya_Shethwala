import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Aerospace Data Insights Platform",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Share+Tech+Mono&display=swap');

/* ── Reset & Root ───────────────────────────────────────── */
#MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }
section[data-testid="stSidebar"] { display: none; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: #020817 !important;
    color: #c8d8f0 !important;
    font-family: 'Rajdhani', sans-serif !important;
}

[data-testid="block-container"], .main .block-container {
    background: transparent !important;
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Starfield BG ───────────────────────────────────────── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 15% 20%, rgba(0, 80, 200, 0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 85% 75%, rgba(30, 0, 120, 0.22) 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 50% 50%, rgba(0, 150, 255, 0.06) 0%, transparent 70%),
        linear-gradient(180deg, #020817 0%, #040d24 40%, #060b1e 100%);
    z-index: 0;
    pointer-events: none;
}

/* ── Grid overlay ───────────────────────────────────────── */
[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(0, 120, 255, 0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 120, 255, 0.04) 1px, transparent 1px);
    background-size: 60px 60px;
    z-index: 0;
    pointer-events: none;
}

/* ── Content wrapper ────────────────────────────────────── */
[data-testid="stVerticalBlock"] {
    position: relative;
    z-index: 1;
}

/* ── Top Navigation ─────────────────────────────────────── */
.top-nav {
    background: rgba(2, 8, 23, 0.92);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(0, 160, 255, 0.2);
    padding: 14px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0;
}

.nav-brand {
    display: flex;
    align-items: center;
    gap: 14px;
}

.nav-icon {
    width: 40px;
    height: 40px;
    background: linear-gradient(135deg, #0066ff, #00c8ff);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    box-shadow: 0 0 20px rgba(0, 150, 255, 0.4);
}

.nav-title {
    font-family: 'Orbitron', monospace;
    font-size: 16px;
    font-weight: 700;
    color: #00c8ff;
    letter-spacing: 2px;
    text-shadow: 0 0 20px rgba(0, 200, 255, 0.5);
}

.nav-subtitle {
    font-family: 'Rajdhani', sans-serif;
    font-size: 11px;
    color: rgba(180, 210, 255, 0.5);
    letter-spacing: 3px;
    text-transform: uppercase;
}

.nav-user {
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(0, 100, 255, 0.08);
    border: 1px solid rgba(0, 160, 255, 0.2);
    border-radius: 24px;
    padding: 8px 16px;
    font-size: 13px;
    color: rgba(180, 210, 255, 0.8);
    font-family: 'Rajdhani', sans-serif;
}

/* ── Login Page ─────────────────────────────────────────── */
.login-hero {
    text-align: center;
    padding: 60px 20px 30px;
}

.login-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0, 100, 255, 0.1);
    border: 1px solid rgba(0, 160, 255, 0.3);
    border-radius: 20px;
    padding: 6px 16px;
    font-family: 'Orbitron', monospace;
    font-size: 10px;
    color: #00c8ff;
    letter-spacing: 3px;
    margin-bottom: 24px;
}

.login-heading {
    font-family: 'Orbitron', monospace;
    font-size: 52px;
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 16px;
    background: linear-gradient(135deg, #ffffff 0%, #a0c4ff 40%, #00c8ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: none;
}

.login-subheading {
    font-size: 16px;
    color: rgba(160, 196, 255, 0.65);
    margin-bottom: 48px;
    letter-spacing: 1px;
}

.login-card {
    background: rgba(5, 15, 40, 0.85);
    backdrop-filter: blur(30px);
    border: 1px solid rgba(0, 120, 255, 0.25);
    border-radius: 20px;
    padding: 36px 40px;
    box-shadow:
        0 0 60px rgba(0, 80, 255, 0.12),
        0 40px 80px rgba(0, 0, 0, 0.4),
        inset 0 1px 0 rgba(255, 255, 255, 0.06);
}

.login-logo-area {
    text-align: center;
    margin-bottom: 28px;
}

.login-logo-icon {
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, #0050ff, #00c8ff);
    border-radius: 18px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin-bottom: 12px;
    box-shadow: 0 0 30px rgba(0, 150, 255, 0.5);
}

.login-brand-name {
    font-family: 'Orbitron', monospace;
    font-size: 22px;
    font-weight: 800;
    color: #00c8ff;
    letter-spacing: 4px;
    display: block;
}

.login-brand-sub {
    font-size: 11px;
    color: rgba(160, 196, 255, 0.5);
    letter-spacing: 3px;
    text-transform: uppercase;
}

.login-divider {
    border: none;
    border-top: 1px solid rgba(0, 100, 255, 0.15);
    margin: 20px 0;
}

.login-demo-note {
    text-align: center;
    font-size: 11px;
    color: rgba(160, 196, 255, 0.4);
    letter-spacing: 1px;
    margin-top: 16px;
}

/* ── Stage Header ───────────────────────────────────────── */
.stage-header {
    padding: 32px 32px 24px;
    border-bottom: 1px solid rgba(0, 100, 255, 0.1);
    margin-bottom: 28px;
}

.stage-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(0, 80, 200, 0.12);
    border: 1px solid rgba(0, 150, 255, 0.25);
    border-radius: 4px;
    padding: 4px 12px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    color: #00a8ff;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.stage-title {
    font-family: 'Orbitron', monospace;
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 1px;
    margin-bottom: 8px;
    line-height: 1.2;
}

.stage-desc {
    font-size: 15px;
    color: rgba(160, 196, 255, 0.55);
    letter-spacing: 0.5px;
}

/* ── Progress bar ───────────────────────────────────────── */
.progress-wrap {
    padding: 0 32px;
    margin-bottom: 4px;
}

.progress-track {
    height: 3px;
    background: rgba(0, 80, 200, 0.15);
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 6px;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #0050ff, #00c8ff);
    border-radius: 2px;
    box-shadow: 0 0 10px rgba(0, 200, 255, 0.6);
    transition: width 0.4s ease;
}

.progress-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    color: rgba(0, 200, 255, 0.5);
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ── Cards ──────────────────────────────────────────────── */
.card {
    background: rgba(4, 12, 35, 0.7);
    border: 1px solid rgba(0, 100, 200, 0.2);
    border-radius: 14px;
    padding: 24px 28px;
    margin: 0 32px 24px;
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0, 180, 255, 0.4), transparent);
}

.card-title {
    font-family: 'Orbitron', monospace;
    font-size: 13px;
    font-weight: 600;
    color: #00c8ff;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ── Physics concept cards ──────────────────────────────── */
.concept-card {
    background: rgba(0, 50, 150, 0.1);
    border: 1px solid rgba(0, 120, 255, 0.2);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
}

.concept-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0, 120, 255, 0.03), transparent);
    pointer-events: none;
}

.concept-icon {
    font-size: 32px;
    margin-bottom: 12px;
    display: block;
    filter: drop-shadow(0 0 10px rgba(0, 180, 255, 0.4));
}

.concept-title {
    font-family: 'Orbitron', monospace;
    font-size: 12px;
    font-weight: 700;
    color: #00c8ff;
    letter-spacing: 2px;
    margin-bottom: 10px;
    text-transform: uppercase;
}

.concept-desc {
    font-size: 13px;
    color: rgba(160, 196, 255, 0.6);
    line-height: 1.6;
}

/* ── Formula box ────────────────────────────────────────── */
.formula-box {
    background: rgba(0, 60, 180, 0.08);
    border: 1px solid rgba(0, 150, 255, 0.2);
    border-left: 3px solid #00c8ff;
    border-radius: 8px;
    padding: 24px 28px;
    text-align: center;
    margin: 16px 0;
}

.formula-label {
    font-size: 13px;
    color: rgba(160, 196, 255, 0.5);
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.formula-main {
    font-family: 'Share Tech Mono', monospace;
    font-size: 28px;
    color: #00c8ff;
    font-weight: 700;
    text-shadow: 0 0 20px rgba(0, 200, 255, 0.4);
    letter-spacing: 4px;
}

.formula-sub {
    font-size: 13px;
    color: rgba(160, 196, 255, 0.6);
    margin-top: 12px;
    line-height: 1.6;
}

/* ── Q&A cards ──────────────────────────────────────────── */
.qa-card {
    background: rgba(0, 40, 120, 0.12);
    border: 1px solid rgba(0, 100, 200, 0.2);
    border-left: 3px solid rgba(0, 150, 255, 0.5);
    border-radius: 8px;
    padding: 18px 20px;
    margin-bottom: 12px;
}

.qa-question {
    font-family: 'Orbitron', monospace;
    font-size: 12px;
    font-weight: 600;
    color: #a0c4ff;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.qa-answer {
    font-size: 13px;
    color: rgba(160, 196, 255, 0.6);
    line-height: 1.5;
    padding-left: 16px;
    border-left: 1px solid rgba(0, 200, 255, 0.2);
}

.qa-check {
    color: #00c8ff;
    font-weight: 700;
    margin-right: 6px;
}

/* ── Metric cards ───────────────────────────────────────── */
[data-testid="stMetric"] {
    background: rgba(0, 40, 130, 0.15) !important;
    border: 1px solid rgba(0, 120, 255, 0.2) !important;
    border-radius: 12px !important;
    padding: 18px 22px !important;
    position: relative !important;
    overflow: hidden !important;
}

[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0, 200, 255, 0.3), transparent);
}

[data-testid="stMetricValue"] {
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 26px !important;
    font-weight: 700 !important;
    color: #00c8ff !important;
    text-shadow: 0 0 15px rgba(0, 200, 255, 0.3) !important;
}

[data-testid="stMetricLabel"] {
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    color: rgba(160, 196, 255, 0.5) !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
}

[data-testid="stMetricDelta"] { display: none !important; }

/* ── Buttons ────────────────────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, #0050d8, #0090ff) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    padding: 14px 28px !important;
    text-transform: uppercase !important;
    transition: all 0.3s !important;
    width: 100% !important;
    position: relative !important;
    overflow: hidden !important;
    box-shadow: 0 4px 20px rgba(0, 100, 255, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(0, 150, 255, 0.5) !important;
}

/* ── Inputs ─────────────────────────────────────────────── */
.stTextInput > div > div > input {
    background: rgba(0, 20, 60, 0.6) !important;
    border: 1px solid rgba(0, 100, 200, 0.3) !important;
    border-radius: 8px !important;
    color: #c8d8f0 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 15px !important;
    padding: 12px 16px !important;
    transition: all 0.3s !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00a8ff !important;
    box-shadow: 0 0 20px rgba(0, 150, 255, 0.15) !important;
    background: rgba(0, 30, 80, 0.7) !important;
}

.stTextInput label {
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    color: rgba(160, 196, 255, 0.6) !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* ── Selectbox ──────────────────────────────────────────── */
.stSelectbox > div > div {
    background: rgba(0, 20, 60, 0.6) !important;
    border: 1px solid rgba(0, 100, 200, 0.3) !important;
    border-radius: 8px !important;
    color: #c8d8f0 !important;
    font-family: 'Rajdhani', sans-serif !important;
}

.stSelectbox label {
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    color: rgba(160, 196, 255, 0.5) !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* ── Slider ─────────────────────────────────────────────── */
.stSlider label {
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    color: rgba(160, 196, 255, 0.6) !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: #00c8ff !important;
}

/* ── Tabs ───────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(2, 8, 23, 0.9) !important;
    border-bottom: 1px solid rgba(0, 100, 200, 0.2) !important;
    gap: 0 !important;
    padding: 0 16px !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: rgba(160, 196, 255, 0.4) !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    padding: 16px 18px !important;
    border-bottom: 2px solid transparent !important;
    transition: all 0.3s !important;
}

.stTabs [aria-selected="true"] {
    color: #00c8ff !important;
    border-bottom: 2px solid #00c8ff !important;
    background: rgba(0, 100, 255, 0.06) !important;
    text-shadow: 0 0 15px rgba(0, 200, 255, 0.4) !important;
}

.stTabs [data-baseweb="tab-panel"] {
    background: transparent !important;
    padding: 0 !important;
}

/* ── Chart wrappers ─────────────────────────────────────── */
.chart-wrap {
    background: rgba(2, 8, 30, 0.6);
    border: 1px solid rgba(0, 80, 200, 0.18);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}

.chart-label {
    font-family: 'Orbitron', monospace;
    font-size: 11px;
    font-weight: 600;
    color: #c8d8f0;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.chart-hint {
    font-size: 11px;
    color: rgba(120, 160, 220, 0.45);
    letter-spacing: 0.5px;
    margin-bottom: 12px;
}

/* ── Divider ────────────────────────────────────────────── */
hr {
    border: none !important;
    border-top: 1px solid rgba(0, 80, 200, 0.12) !important;
    margin: 8px 32px !important;
}

/* ── Scrollbar ──────────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: rgba(0, 20, 60, 0.3); }
::-webkit-scrollbar-thumb { background: rgba(0, 120, 255, 0.3); border-radius: 3px; }

/* ── Columns padding ────────────────────────────────────── */
[data-testid="column"] {
    padding: 4px 8px !important;
}

/* ── Caption ────────────────────────────────────────────── */
.stCaption {
    font-family: 'Share Tech Mono', monospace !important;
    color: rgba(120, 160, 220, 0.45) !important;
    font-size: 11px !important;
    letter-spacing: 0.5px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Dataset ──────────────────────────────────────────────────────────────────
mock_data = [
    {"id": 1,  "mission": "SpaceX Crew-1",          "type": "Crewed",   "cost": 62,  "payload": 5800,  "fuel": 450000,  "duration": 28,  "crew": 4, "success": "Yes", "target": "LEO",  "vehicle": "Falcon 9",  "year": 2020, "distance": 408},
    {"id": 2,  "mission": "Blue Origin New Shepard", "type": "Uncrewed", "cost": 28,  "payload": 3600,  "fuel": 280000,  "duration": 10,  "crew": 0, "success": "Yes", "target": "LEO",  "vehicle": "New Shepard","year": 2021, "distance": 100},
    {"id": 3,  "mission": "Ariane 5 ECA",            "type": "Uncrewed", "cost": 165, "payload": 10200, "fuel": 650000,  "duration": 45,  "crew": 0, "success": "Yes", "target": "GEO",  "vehicle": "Ariane 5",  "year": 2022, "distance": 36000},
    {"id": 4,  "mission": "Delta IV Heavy",           "type": "Uncrewed", "cost": 350, "payload": 28800, "fuel": 950000,  "duration": 180, "crew": 0, "success": "Yes", "target": "Moon", "vehicle": "Delta IV",   "year": 2023, "distance": 384400},
    {"id": 5,  "mission": "SpaceX Falcon Heavy",      "type": "Uncrewed", "cost": 90,  "payload": 63800, "fuel": 1200000, "duration": 365, "crew": 0, "success": "Yes", "target": "Mars", "vehicle": "Falcon 9",  "year": 2021, "distance": 54600000},
    {"id": 6,  "mission": "Soyuz MS-19",              "type": "Crewed",   "cost": 45,  "payload": 7500,  "fuel": 380000,  "duration": 180, "crew": 3, "success": "Yes", "target": "LEO",  "vehicle": "Soyuz",     "year": 2022, "distance": 408},
    {"id": 7,  "mission": "Atlas V 541",              "type": "Uncrewed", "cost": 185, "payload": 8900,  "fuel": 620000,  "duration": 60,  "crew": 0, "success": "No",  "target": "GEO",  "vehicle": "Atlas V",   "year": 2020, "distance": 35800},
    {"id": 8,  "mission": "JAXA H-IIA",               "type": "Uncrewed", "cost": 75,  "payload": 4200,  "fuel": 400000,  "duration": 25,  "crew": 0, "success": "Yes", "target": "LEO",  "vehicle": "H-IIA",     "year": 2023, "distance": 450},
    {"id": 9,  "mission": "SpaceX Crew-2",            "type": "Crewed",   "cost": 60,  "payload": 5900,  "fuel": 460000,  "duration": 28,  "crew": 4, "success": "Yes", "target": "LEO",  "vehicle": "Falcon 9",  "year": 2021, "distance": 410},
    {"id": 10, "mission": "Vega C",                   "type": "Uncrewed", "cost": 32,  "payload": 2500,  "fuel": 240000,  "duration": 15,  "crew": 0, "success": "Yes", "target": "LEO",  "vehicle": "Vega",      "year": 2022, "distance": 500},
    {"id": 11, "mission": "ULA Vulcan",               "type": "Uncrewed", "cost": 110, "payload": 9600,  "fuel": 700000,  "duration": 50,  "crew": 0, "success": "No",  "target": "Moon", "vehicle": "Vulcan",    "year": 2023, "distance": 380000},
    {"id": 12, "mission": "ISRO LVM3",                "type": "Uncrewed", "cost": 40,  "payload": 6000,  "fuel": 420000,  "duration": 30,  "crew": 0, "success": "Yes", "target": "LEO",  "vehicle": "LVM3",      "year": 2021, "distance": 600},
]
df_full = pd.DataFrame(mock_data)

# ─── Session State ────────────────────────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# ─── Plotly theme helper ───────────────────────────────────────────────────────
def styled_fig(fig, height=300):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Rajdhani, sans-serif", color="#8aa8d0", size=12),
        margin=dict(l=10, r=10, t=20, b=10),
        legend=dict(font=dict(color="#8aa8d0", size=11)),
        height=height,
    )
    fig.update_xaxes(
        gridcolor="rgba(0,80,200,0.1)",
        linecolor="rgba(0,100,200,0.15)",
        tickfont=dict(color="#6888aa", size=11),
        title_font=dict(color="#8aa8d0", size=12),
        zeroline=False,
    )
    fig.update_yaxes(
        gridcolor="rgba(0,80,200,0.1)",
        linecolor="rgba(0,100,200,0.15)",
        tickfont=dict(color="#6888aa", size=11),
        title_font=dict(color="#8aa8d0", size=12),
        zeroline=False,
    )
    return fig

# ─── LOGIN SCREEN ─────────────────────────────────────────────────────────────
if not st.session_state.logged_in:

    # Hero section
    st.markdown("""
    <div class="login-hero">
        <div class="login-badge">🛰️ &nbsp; MISSION CONTROL SYSTEM &nbsp; v2.4</div>
        <div class="login-heading">AEROSPACE<br>DATA INSIGHTS</div>
        <div class="login-subheading">Advanced space mission analytics & rocket simulation platform</div>
    </div>
    """, unsafe_allow_html=True)

    # Login card — centred using columns
    col_l, col_m, col_r = st.columns([1, 1.1, 1])
    with col_m:
        st.markdown("""
        <div class="login-card">
            <div class="login-logo-area">
                <div class="login-logo-icon">🚀</div>
                <span class="login-brand-name">AEROSPACE</span>
                <span class="login-brand-sub">Data Insights Platform</span>
            </div>
            <hr class="login-divider">
        </div>
        """, unsafe_allow_html=True)

        email = st.text_input("Email Address", placeholder="commander@nasa.gov", key="login_email")
        password = st.text_input("Access Code", placeholder="••••••••••••", type="password", key="login_password")
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("INITIATE LOGIN SEQUENCE", key="login_btn"):
            if email and password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("⚠ Please enter credentials to proceed")

        st.markdown('<div class="login-demo-note">DEMO MODE — Any credentials accepted</div>', unsafe_allow_html=True)


# ─── MAIN DASHBOARD ───────────────────────────────────────────────────────────
else:
    # Top Navigation
    st.markdown(f"""
    <div class="top-nav">
        <div class="nav-brand">
            <div class="nav-icon">🛰️</div>
            <div>
                <div class="nav-title">AEROSPACE DATA INSIGHTS</div>
                <div class="nav-subtitle">Mission Analytics Platform</div>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:16px;">
            <div style="font-family:'Share Tech Mono',monospace; font-size:11px; color:rgba(0,200,255,0.5);">
                SYS:ONLINE &nbsp;|&nbsp; DATA:LIVE
            </div>
            <div class="nav-user">
                👤 &nbsp; {st.session_state.user_email}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "01  FUNDAMENTALS",
        "02  DATA ANALYSIS",
        "03  VISUALIZATIONS",
        "04  SIMULATION"
    ])

    # ─── TAB 1: UNDERSTANDING ────────────────────────────────────────────────
    with tab1:
        st.markdown("""
        <div class="progress-wrap">
            <div class="progress-track"><div class="progress-fill" style="width:25%"></div></div>
            <div class="progress-label">Stage 1 of 4 &nbsp;·&nbsp; 25% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">📚 Stage 01</div>
            <div class="stage-title">Understanding Rocket Dynamics</div>
            <div class="stage-desc">Master the fundamental physics governing rocket launches before analyzing real mission data</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">⚡ Newton's Second Law of Motion</div>
            <p style="font-size:15px; color:rgba(180,210,255,0.75); line-height:1.9; margin-bottom:20px;">
                Rocket motion is governed by <strong style="color:#a0c8ff;">Newton's Second Law of Motion</strong>, which states:
            </p>
            <div class="formula-box" style="margin-bottom:20px;">
                <div class="formula-label">The Fundamental Principle</div>
                <div class="formula-main">Force = Mass × Acceleration</div>
            </div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.8; margin-bottom:20px;">
                This means that acceleration depends on the <strong style="color:#a0c8ff;">net force</strong> acting on the rocket divided by its <strong style="color:#a0c8ff;">mass</strong>. The mathematical expression for rocket acceleration is:
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">📐 Rocket Acceleration Equation</div>
        """, unsafe_allow_html=True)

        fa1, fa2 = st.columns([1.1, 1])
        with fa1:
            st.markdown("""
            <div class="formula-box" style="margin-bottom:16px;">
                <div class="formula-label">Acceleration Formula</div>
                <div style="display:inline-flex; align-items:center; gap:14px; justify-content:center; width:100%; padding:8px 0;">
                    <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:28px; color:#00c8ff; text-shadow:0 0 16px rgba(0,200,255,0.4);">a</span>
                    <span style="font-size:26px; color:rgba(160,196,255,0.5); font-weight:300;">=</span>
                    <div style="display:inline-flex; flex-direction:column; align-items:center; gap:0;">
                        <div style="font-family:'Georgia','Times New Roman',serif; font-size:22px; color:#e0f0ff; padding-bottom:6px; letter-spacing:1px; white-space:nowrap;">
                            <span style="font-style:italic; color:#00c8ff;">T</span>
                            <span style="color:rgba(160,196,255,0.6); margin:0 6px;">−</span>
                            <span style="color:rgba(160,196,255,0.5);">(</span><span style="font-style:italic; color:#ff8888;">m</span><span style="font-style:italic; color:#ff8888;">g</span>
                            <span style="color:rgba(160,196,255,0.5); margin:0 5px;">+</span>
                            <span style="font-style:italic; color:#ffaa40;">D</span><span style="color:rgba(160,196,255,0.5);">)</span>
                        </div>
                        <div style="width:100%; height:2px; background:linear-gradient(90deg, transparent, rgba(0,200,255,0.7), transparent); border-radius:1px;"></div>
                        <div style="font-family:'Georgia','Times New Roman',serif; font-size:22px; font-style:italic; color:#ff8888; padding-top:6px;">
                            m
                        </div>
                    </div>
                </div>
            </div>
            <div style="background:rgba(0,40,120,0.18); border:1px solid rgba(0,100,200,0.2); border-radius:10px; padding:18px 20px;">
                <div style="font-family:'Orbitron',monospace; font-size:10px; color:#00a8ff; letter-spacing:2px; margin-bottom:14px;">VARIABLE LEGEND</div>
                <div style="display:flex; flex-direction:column; gap:10px;">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:17px; color:#00c8ff; min-width:32px;">T</span>
                        <span style="font-size:13px; color:rgba(160,196,255,0.7);">= Thrust</span>
                    </div>
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:17px; color:#ff8888; min-width:32px;">mg</span>
                        <span style="font-size:13px; color:rgba(160,196,255,0.7);">= Weight (gravity force)</span>
                    </div>
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:17px; color:#ffaa40; min-width:32px;">D</span>
                        <span style="font-size:13px; color:rgba(160,196,255,0.7);">= Drag</span>
                    </div>
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:17px; color:#ff8888; min-width:32px;">m</span>
                        <span style="font-size:13px; color:rgba(160,196,255,0.7);">= mass</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with fa2:
            st.markdown("""
            <div style="background:rgba(0,30,100,0.2); border:1px solid rgba(0,100,200,0.2); border-radius:10px; padding:20px; height:100%;">
                <div style="font-family:'Orbitron',monospace; font-size:10px; color:#00a8ff; letter-spacing:2px; margin-bottom:16px;">FORCE DIAGRAM</div>
                <div style="text-align:center; padding:10px 0;">
                    <div style="font-size:13px; color:rgba(0,220,120,0.9); letter-spacing:1px; margin-bottom:8px;">▲ &nbsp; THRUST (T)</div>
                    <div style="font-size:11px; color:rgba(160,196,255,0.4); margin-bottom:4px;">pushes rocket upward</div>
                    <div style="width:3px; height:40px; background:linear-gradient(180deg,rgba(0,220,120,0.6),rgba(0,200,255,0.2)); margin:8px auto;"></div>
                    <div style="width:60px; height:60px; background:linear-gradient(135deg,rgba(0,100,255,0.2),rgba(60,40,200,0.3)); border:1px solid rgba(0,150,255,0.3); border-radius:8px; margin:0 auto; display:flex; align-items:center; justify-content:center;">
                        <span style="font-size:22px;">🚀</span>
                    </div>
                    <div style="width:3px; height:40px; background:linear-gradient(180deg,rgba(255,80,80,0.2),rgba(255,60,60,0.6)); margin:8px auto;"></div>
                    <div style="font-size:11px; color:rgba(160,196,255,0.4); margin-bottom:4px;">pulls rocket downward</div>
                    <div style="font-size:13px; color:rgba(255,100,100,0.9); letter-spacing:1px;">▼ &nbsp; GRAVITY (mg) + DRAG (D)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">🔬 Three Primary Forces Acting on a Rocket</div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.7; margin-bottom:20px;">
                During launch, three fundamental forces determine a rocket's trajectory and performance:
            </p>
        </div>
        """, unsafe_allow_html=True)

        fc1, fc2, fc3 = st.columns(3)
        forces = [
            ("⬆️", "THRUST", "#00cc80", "rgba(0,180,100,0.15)", "rgba(0,150,80,0.25)",
             "Produced by the rocket engine, it pushes the rocket <strong style='color:#80ffcc;'>upward</strong>. Generated by burning propellant and expelling hot gases at high velocity through the nozzle.",
             "1"),
            ("⬇️", "GRAVITY", "#ff6060", "rgba(220,60,60,0.15)", "rgba(200,40,40,0.25)",
             "Pulls the rocket <strong style='color:#ffaaaa;'>downward</strong> toward Earth at a constant <strong style='color:#ffaaaa;'>9.81 m/s²</strong>. Must be continuously overcome by thrust to gain or maintain altitude.",
             "2"),
            ("🌀", "DRAG", "#ffaa40", "rgba(220,140,0,0.15)", "rgba(200,120,0,0.25)",
             "Air resistance that <strong style='color:#ffd080;'>opposes upward motion</strong>. Strongest near Earth, decreases at higher altitudes due to reduced air density. Becomes negligible above 80 km.",
             "3"),
        ]
        for col, (icon, title, color, bg, border_c, desc, num) in zip([fc1, fc2, fc3], forces):
            with col:
                st.markdown(f"""
                <div style="background:{bg}; border:1px solid {border_c}; border-radius:14px; padding:24px 20px; text-align:center; height:100%;">
                    <div style="width:36px; height:36px; background:{border_c}; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; font-family:'Orbitron',monospace; font-size:13px; font-weight:700; color:{color}; margin-bottom:14px;">{num}</div>
                    <div style="font-size:32px; margin-bottom:10px; filter:drop-shadow(0 0 8px {color}80);">{icon}</div>
                    <div style="font-family:'Orbitron',monospace; font-size:13px; font-weight:700; color:{color}; letter-spacing:2px; margin-bottom:12px;">{title}</div>
                    <div style="font-size:13px; color:rgba(180,210,255,0.65); line-height:1.7;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-top:24px;">
            <div class="card-title">🌬️ Drag Force Equation</div>
        """, unsafe_allow_html=True)
        d1, d2 = st.columns([1, 1.2])
        with d1:
            st.markdown("""
            <div class="formula-box">
                <div class="formula-label">The Drag Equation</div>
                <div style="display:inline-flex; align-items:center; gap:12px; justify-content:center; width:100%; padding:10px 0; flex-wrap:wrap;">
                    <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:26px; color:#00c8ff; text-shadow:0 0 14px rgba(0,200,255,0.4);">Drag</span>
                    <span style="font-size:24px; color:rgba(160,196,255,0.5); font-weight:300;">=</span>
                    <div style="display:inline-flex; flex-direction:column; align-items:center;">
                        <div style="font-family:'Georgia','Times New Roman',serif; font-size:17px; color:#e0f0ff; padding-bottom:4px; line-height:1;">1</div>
                        <div style="width:100%; height:2px; background:linear-gradient(90deg,rgba(0,200,255,0.6),rgba(0,200,255,0.6)); border-radius:1px; min-width:14px;"></div>
                        <div style="font-family:'Georgia','Times New Roman',serif; font-size:17px; color:#e0f0ff; padding-top:4px; line-height:1;">2</div>
                    </div>
                    <div style="display:inline-flex; align-items:baseline; gap:4px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:26px; color:#ffaa40;">C</span><span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:18px; color:#ffaa40; vertical-align:sub; margin-left:-4px;">d</span>
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:26px; color:#00cc80; margin-left:4px;">ρ</span>
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:26px; color:#a080ff; margin-left:4px;">A</span>
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:26px; color:#00c8ff; margin-left:4px;">v</span><span style="font-family:'Georgia','Times New Roman',serif; font-size:16px; color:#00c8ff; vertical-align:super; margin-left:-2px;">2</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with d2:
            st.markdown("""
            <div style="padding:8px 0;">
                <div style="font-family:'Orbitron',monospace; font-size:10px; color:#00a8ff; letter-spacing:2px; margin-bottom:14px;">DRAG VARIABLE BREAKDOWN</div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                    <div style="background:rgba(0,40,120,0.15); border:1px solid rgba(0,80,180,0.2); border-radius:8px; padding:10px 12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; color:#ffaa40; font-size:17px;">C<sub style="font-size:12px;">d</sub></span>
                        <div style="font-size:12px; color:rgba(160,196,255,0.6); margin-top:4px;">Drag coefficient</div>
                    </div>
                    <div style="background:rgba(0,40,120,0.15); border:1px solid rgba(0,80,180,0.2); border-radius:8px; padding:10px 12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; color:#00cc80; font-size:17px;">ρ</span>
                        <div style="font-size:12px; color:rgba(160,196,255,0.6); margin-top:4px;">Air density (kg/m³)</div>
                    </div>
                    <div style="background:rgba(0,40,120,0.15); border:1px solid rgba(0,80,180,0.2); border-radius:8px; padding:10px 12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; color:#a080ff; font-size:17px;">A</span>
                        <div style="font-size:12px; color:rgba(160,196,255,0.6); margin-top:4px;">Cross-sectional area</div>
                    </div>
                    <div style="background:rgba(0,40,120,0.15); border:1px solid rgba(0,80,180,0.2); border-radius:8px; padding:10px 12px;">
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; color:#00c8ff; font-size:17px;">v<sup style="font-size:12px;">2</sup></span>
                        <div style="font-size:12px; color:rgba(160,196,255,0.6); margin-top:4px;">Velocity squared</div>
                    </div>
                </div>
                <div style="margin-top:12px; font-size:12px; color:rgba(160,196,255,0.5); font-style:italic;">
                    › As altitude increases, air density (ρ) decreases → drag force reduces significantly
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">🔥 Fuel Consumption & Mass Reduction</div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.8; margin-bottom:16px;">
                As fuel burns, the rocket's <strong style="color:#a0c8ff;">total mass decreases continuously</strong>. Since acceleration equals
                force divided by mass (<span style="font-family:'Share Tech Mono',monospace; color:#00c8ff;">a = F/m</span>),
                a lower mass results in <strong style="color:#a0c8ff;">higher acceleration</strong> even with the same thrust force.
                This explains why rockets <em style="color:#80c8ff;">accelerate faster as fuel is consumed</em> — the engine output stays
                constant while the rocket grows lighter.
            </p>
            <div style="display:flex; gap:16px; flex-wrap:wrap;">
                <div style="flex:1; min-width:180px; background:rgba(0,50,150,0.12); border:1px solid rgba(0,100,200,0.2); border-radius:10px; padding:16px 18px; text-align:center;">
                    <div style="font-family:'Share Tech Mono',monospace; font-size:22px; color:#00c8ff; margin-bottom:6px;">m ↓</div>
                    <div style="font-size:12px; color:rgba(160,196,255,0.55);">Mass decreases<br>as fuel burns</div>
                </div>
                <div style="display:flex; align-items:center; font-size:22px; color:rgba(100,160,255,0.4);">→</div>
                <div style="flex:1; min-width:180px; background:rgba(0,50,150,0.12); border:1px solid rgba(0,100,200,0.2); border-radius:10px; padding:16px 18px; text-align:center;">
                    <div style="font-family:'Share Tech Mono',monospace; font-size:22px; color:#80a0ff; margin-bottom:6px;">F = const</div>
                    <div style="font-size:12px; color:rgba(160,196,255,0.55);">Thrust force<br>remains steady</div>
                </div>
                <div style="display:flex; align-items:center; font-size:22px; color:rgba(100,160,255,0.4);">→</div>
                <div style="flex:1; min-width:180px; background:rgba(0,180,100,0.08); border:1px solid rgba(0,180,100,0.2); border-radius:10px; padding:16px 18px; text-align:center;">
                    <div style="font-family:'Share Tech Mono',monospace; font-size:22px; color:#00cc80; margin-bottom:6px;">a ↑↑</div>
                    <div style="font-size:12px; color:rgba(160,196,255,0.55);">Acceleration<br>increases!</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">🔗 Connection to Dataset</div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.8; margin-bottom:20px;">
                The provided mission dataset contains real-world variables that directly reflect these physics principles:
            </p>
        </div>
        """, unsafe_allow_html=True)

        ds1, ds2 = st.columns(2)
        dataset_vars = [
            ("📦", "Payload Weight", "Directly affects total mass — higher payload increases required thrust and fuel consumption"),
            ("⛽", "Fuel Consumption", "Tied to payload weight, mission distance, and thrust requirements"),
            ("💰", "Mission Cost", "Often related to fuel usage, vehicle complexity, and mission distance"),
            ("⏱️", "Mission Duration", "Influenced by distance from Earth and propulsion efficiency"),
        ]
        for i, (icon, var, detail) in enumerate(dataset_vars):
            col = ds1 if i % 2 == 0 else ds2
            with col:
                st.markdown(f"""
                <div style="background:rgba(0,40,130,0.12); border:1px solid rgba(0,90,200,0.18); border-left:3px solid rgba(0,160,255,0.4); border-radius:8px; padding:14px 18px; margin-bottom:12px;">
                    <div style="font-family:'Orbitron',monospace; font-size:11px; color:#a0c8ff; letter-spacing:1px; margin-bottom:6px;">{icon} &nbsp; {var}</div>
                    <div style="font-size:13px; color:rgba(160,196,255,0.6); line-height:1.6;">{detail}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin:0 32px; background:rgba(0,60,180,0.08); border:1px solid rgba(0,100,200,0.18); border-radius:8px; padding:14px 20px;">
            <span style="font-size:13px; color:rgba(160,196,255,0.6);">
                › <strong style="color:#a0c8ff;">Mission success</strong> may depend on the optimal balance between thrust, fuel capacity, and payload weight — confirming that physics governs real-world outcomes.
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-top:24px;">
            <div class="card-title">❓ Guiding Questions</div>
        """, unsafe_allow_html=True)

        guiding = [
            ("Q1", "How does adding more payload affect altitude?",
             "Increasing payload increases mass, which reduces acceleration. More thrust and fuel are required to reach higher altitudes. The relationship is directly governed by a = F/m."),
            ("Q2", "How does increasing thrust affect launch success?",
             "Higher thrust increases net force, improving acceleration and the ability to overcome gravity quickly. This directly correlates with higher success rates in our dataset."),
            ("Q3", "Does lower drag at higher altitudes improve speed?",
             "Yes — reduced air density decreases drag force (Drag = ½CdρAv²), allowing the rocket to move more efficiently. This is why rockets gain speed rapidly above 50 km."),
            ("Q4", "Can simulation values be compared to real mission data?",
             "Yes. Trends observed in simulation — such as higher payload requiring more fuel — can be directly validated using real-world dataset patterns in Stages 2 and 3."),
        ]
        for tag, q, a in guiding:
            st.markdown(f"""
            <div class="qa-card">
                <div class="qa-question">[{tag}] &nbsp; {q}</div>
                <div class="qa-answer"><span class="qa-check">›</span>{a}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin:0 32px 32px; background:linear-gradient(135deg, rgba(0,60,200,0.12), rgba(40,0,160,0.1)); border:1px solid rgba(0,120,255,0.2); border-radius:14px; padding:28px 32px; position:relative; overflow:hidden;">
            <div style="position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg, transparent, rgba(0,180,255,0.5), rgba(100,60,255,0.5), transparent);"></div>
            <div style="font-family:'Orbitron',monospace; font-size:12px; font-weight:700; color:#00c8ff; letter-spacing:2px; text-transform:uppercase; margin-bottom:14px;">🌍 Real-World Importance</div>
            <p style="font-size:14px; color:rgba(180,210,255,0.72); line-height:1.9; margin:0;">
                Understanding these dynamics helps aerospace engineers
                <strong style="color:#a0c8ff;">design efficient rockets</strong>,
                <strong style="color:#a0c8ff;">estimate accurate fuel requirements</strong>,
                <strong style="color:#a0c8ff;">reduce mission costs</strong>, and
                <strong style="color:#a0c8ff;">increase launch success probability</strong>.
                The physics principles covered in this stage form the foundation for all analysis in the remaining stages —
                from interpreting the dataset patterns in Stage 2, to validating simulation outputs in Stage 4.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ─── TAB 2: DATA ANALYSIS ────────────────────────────────────────────────
    with tab2:
        st.markdown("""
        <div class="progress-wrap">
            <div class="progress-track"><div class="progress-fill" style="width:50%"></div></div>
            <div class="progress-label">Stage 2 of 4 &nbsp;·&nbsp; 50% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">📊 Stage 02</div>
            <div class="stage-title">Data Preprocessing & Cleaning</div>
            <div class="stage-desc">The dataset was carefully examined and cleaned to ensure accuracy and reliability before analysis</div>
        </div>
        """, unsafe_allow_html=True)

        steps = [
            ("01", "Loaded Dataset", "#00c8ff",
             "df = pd.read_csv('rocket_missions.csv')",
             "df.head()  ·  df.info()  ·  df.describe()",
             [
                 ("<b>head()</b> — previews first 5 rows to confirm columns loaded correctly", ),
                 ("<b>info()</b> — reveals data types and which columns have missing values", ),
                 ("<b>describe()</b> — shows min, max, mean to detect outliers or unrealistic values", ),
             ]),
            ("02", "Converted Data Types", "#80a0ff",
             "df['Launch Date'] = pd.to_datetime(df['Launch Date'], errors='coerce')",
             "pd.to_numeric()  ·  errors='coerce'  ·  .dt.year",
             [
                 ("Launch Date converted to <b>datetime</b> — enables year filtering and time-series analysis", ),
                 ("Numeric columns (cost, payload, fuel, duration, distance, crew) converted using <b>pd.to_numeric()</b>", ),
                 ("<b>errors='coerce'</b> turns invalid entries into NaN instead of crashing the program", ),
             ]),
            ("03", "Handled Missing Values", "#ffaa40",
             "df.isnull().sum()",
             "dropna()  ·  fillna(median)",
             [
                 ("<b>isnull().sum()</b> — counts null entries per column to identify gaps", ),
                 ("<b>dropna()</b> — removes rows where critical fields like mission name or success are missing", ),
                 ("<b>fillna(median)</b> — fills numeric gaps with the median to preserve data without distortion", ),
             ]),
            ("04", "Removed Duplicates", "#ff6080",
             "df = df.drop_duplicates()",
             "reset_index(drop=True)",
             [
                 ("Duplicate rows inflate counts and skew success rate calculations", ),
                 ("<b>drop_duplicates()</b> ensures each mission record appears exactly once", ),
                 ("<b>reset_index()</b> restores a clean 0, 1, 2… index after rows were removed", ),
             ]),
            ("05", "Understood What Was Cleaned", "#00cc80",
             "df['year'] = df['Launch Date'].dt.year",
             "launch year extracted for slider filtering",
             [
                 ("Launch year extracted into its own column to power the year-range slider", ),
                 ("Clean data ensures <b>charts render correctly</b> and statistics are not distorted", ),
                 ("Cleaned dataset is now ready for visualization and simulation comparison", ),
             ]),
        ]

        for step in steps:
            num, title, color, code1, code2, bullets = step
            bullet_html = "".join([
                f'<div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:8px;"><span style="color:{color};font-size:15px;line-height:1.3;">›</span><span style="font-size:13px;color:rgba(180,210,255,0.68);line-height:1.6;">{b[0]}</span></div>'
                for b in bullets
            ])
            st.markdown(f"""
            <div style="margin:0 32px 16px; background:rgba(2,8,28,0.6); border:1px solid rgba(0,80,180,0.18); border-left:3px solid {color}; border-radius:12px; padding:22px 26px; position:relative;">
                <div style="display:flex; align-items:center; gap:14px; margin-bottom:16px;">
                    <div style="width:34px; height:34px; background:rgba(0,60,180,0.2); border:1px solid {color}50; border-radius:8px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron',monospace; font-size:12px; color:{color}; flex-shrink:0; font-weight:700;">{num}</div>
                    <div style="font-family:'Orbitron',monospace; font-size:13px; font-weight:700; color:{color}; letter-spacing:1.5px;">{title}</div>
                </div>
                <div style="display:flex; gap:20px; flex-wrap:wrap; margin-bottom:16px;">
                    <div style="background:rgba(0,10,30,0.6); border:1px solid rgba(0,60,140,0.25); border-radius:6px; padding:9px 14px; flex:1; min-width:200px;">
                        <span style="font-family:'Share Tech Mono',monospace; font-size:12px; color:{color}cc; line-height:1.6;">{code1}</span>
                    </div>
                    <div style="background:rgba(0,10,30,0.4); border:1px solid rgba(0,50,120,0.2); border-radius:6px; padding:9px 14px; flex:1; min-width:180px;">
                        <span style="font-family:'Share Tech Mono',monospace; font-size:11px; color:rgba(140,180,255,0.5); line-height:1.6;">{code2}</span>
                    </div>
                </div>
                <div>{bullet_html}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin:24px 32px 0; border-top:1px solid rgba(0,80,200,0.15); padding-top:24px;">
            <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00a8ff; letter-spacing:2px; margin-bottom:16px;">📋 CLEANED DATASET — LIVE PREVIEW</div>
        </div>
        """, unsafe_allow_html=True)

        fc1, fc2 = st.columns(2)
        with fc1:
            mission_type = st.selectbox("Mission Type", ["All Types", "Crewed", "Uncrewed"], key="s2_type")
        with fc2:
            vehicle = st.selectbox("Launch Vehicle", ["All Vehicles", "Falcon 9", "Atlas V", "Ariane 5", "Soyuz"], key="s2_vehicle")
        year_range = st.slider("Year Range", min_value=2020, max_value=2023, value=(2020, 2023), key="s2_year")

        df = df_full.copy()
        if mission_type != "All Types":
            df = df[df["type"] == mission_type]
        if vehicle != "All Vehicles":
            df = df[df["vehicle"] == vehicle]
        df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]
        if len(df) == 0:
            df = df_full.copy()

        total = len(df)
        success_rate = (df["success"] == "Yes").sum() / total * 100
        avg_cost = df["cost"].mean()
        avg_duration = df["duration"].mean()

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Missions", total)
        m2.metric("Success Rate", f"{success_rate:.0f}%")
        m3.metric("Avg. Cost", f"${avg_cost:.1f}M")
        m4.metric("Avg. Duration", f"{avg_duration:.1f}d")

        # ── Inject table CSS separately (no f-string, avoids brace conflicts) ──
        st.markdown("""
        <style>
        .custom-table-wrap {
            margin: 0 0 8px 0;
            border: 1px solid rgba(0, 100, 200, 0.25);
            border-radius: 12px;
            overflow: hidden;
            background: rgba(2, 8, 30, 0.92);
        }
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Rajdhani', sans-serif;
            font-size: 14px;
            background: transparent;
        }
        .custom-table thead tr {
            background: rgba(0, 40, 120, 0.5);
            border-bottom: 1px solid rgba(0, 120, 255, 0.25);
        }
        .custom-table thead th {
            padding: 13px 16px;
            text-align: left;
            font-family: 'Orbitron', monospace;
            font-size: 10px;
            font-weight: 700;
            color: #00c8ff;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            white-space: nowrap;
        }
        .custom-table .data-row {
            border-bottom: 1px solid rgba(0, 60, 150, 0.15);
            transition: background 0.2s;
        }
        .custom-table .data-row:last-child {
            border-bottom: none;
        }
        .custom-table .data-row:hover {
            background: rgba(0, 80, 200, 0.1) !important;
        }
        .custom-table .data-row:nth-child(even) {
            background: rgba(0, 20, 60, 0.3);
        }
        .custom-table .data-row:nth-child(odd) {
            background: transparent;
        }
        .custom-table td {
            padding: 12px 16px;
            color: rgba(160, 196, 255, 0.8);
            vertical-align: middle;
        }
        </style>
        """, unsafe_allow_html=True)

        # ── Build rows HTML as plain string (no CSS braces to conflict with) ──
        rows_html = ""
        for _, row in df.iterrows():
            s_color = "#00c8ff" if row["success"] == "Yes" else "#ff4466"
            s_bg    = "rgba(0,200,255,0.08)" if row["success"] == "Yes" else "rgba(255,60,100,0.08)"
            s_border = s_color + "40"
            type_val    = str(row['type']).upper()
            mission_val = str(row['mission'])
            cost_val    = "$" + str(row['cost']) + "M"
            payload_val = "{:,}".format(int(row['payload']))
            fuel_val    = "{:,}".format(int(row['fuel']))
            dur_val     = str(row['duration'])
            succ_val    = str(row['success']).upper()
            year_val    = str(row['year'])

            rows_html += (
                '<tr class="data-row">'
                '<td style="font-weight:600;color:#c8d8f0;">' + mission_val + '</td>'
                '<td><span style="background:rgba(0,100,200,0.15);border:1px solid rgba(0,120,255,0.2);border-radius:4px;padding:3px 10px;font-size:12px;color:#80b0ff;font-family:Share Tech Mono,monospace;letter-spacing:1px;">' + type_val + '</span></td>'
                '<td style="color:#a0c8ff;font-family:Share Tech Mono,monospace;">' + cost_val + '</td>'
                '<td style="color:#c8d8f0;font-family:Share Tech Mono,monospace;">' + payload_val + '</td>'
                '<td style="color:#c8d8f0;font-family:Share Tech Mono,monospace;">' + fuel_val + '</td>'
                '<td style="color:#c8d8f0;font-family:Share Tech Mono,monospace;">' + dur_val + '</td>'
                '<td><span style="background:' + s_bg + ';border:1px solid ' + s_border + ';border-radius:4px;padding:3px 10px;font-size:12px;color:' + s_color + ';font-family:Share Tech Mono,monospace;font-weight:700;">' + succ_val + '</span></td>'
                '<td style="color:rgba(160,196,255,0.6);font-family:Share Tech Mono,monospace;">' + year_val + '</td>'
                '</tr>'
            )

        # ── Render the table as plain HTML string (no f-string interpolation) ──
        table_html = (
            '<div class="custom-table-wrap">'
            '<table class="custom-table">'
            '<thead><tr>'
            '<th>Mission Name</th><th>Type</th><th>Cost ($M)</th>'
            '<th>Payload (kg)</th><th>Fuel (L)</th><th>Duration (days)</th>'
            '<th>Success</th><th>Year</th>'
            '</tr></thead>'
            '<tbody>' + rows_html + '</tbody>'
            '</table></div>'
        )
        st.markdown(table_html, unsafe_allow_html=True)

        st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)

    # ─── TAB 3: VISUALIZATIONS ───────────────────────────────────────────────
    with tab3:
        st.markdown("""
        <div class="progress-wrap">
            <div class="progress-track"><div class="progress-fill" style="width:75%"></div></div>
            <div class="progress-label">Stage 3 of 4 &nbsp;·&nbsp; 75% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">📈 Stage 03</div>
            <div class="stage-title">Interactive Visualizations</div>
            <div class="stage-desc">Analyze relationships between rocket characteristics and mission outcomes across 5 charts</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">🔬 Chart Filter</div>', unsafe_allow_html=True)
        chart_filter = st.selectbox("Display Missions", ["All Missions", "Successful Only", "Failed Only"], key="chart_filter")
        st.markdown('</div>', unsafe_allow_html=True)

        chart_df = df_full.copy()
        if chart_filter == "Successful Only":
            chart_df = chart_df[chart_df["success"] == "Yes"]
        elif chart_filter == "Failed Only":
            chart_df = chart_df[chart_df["success"] == "No"]
        if len(chart_df) == 0:
            chart_df = df_full.copy()

        success_df = chart_df[chart_df["success"] == "Yes"]
        fail_df = chart_df[chart_df["success"] == "No"]

        cc1, cc2 = st.columns(2)

        with cc1:
            st.markdown('<div style="margin:0 16px 0 32px;">', unsafe_allow_html=True)
            st.markdown("""
            <div class="chart-label">Chart 01 · Payload vs Fuel Consumption</div>
            <div class="chart-hint">💡 Heavier payload → More fuel required</div>
            """, unsafe_allow_html=True)
            colors = ["#00c8ff" if s == "Yes" else "#ff4466" for s in chart_df["success"]]
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(
                x=chart_df["payload"], y=chart_df["fuel"],
                mode="markers",
                marker=dict(
                    color=colors, size=11,
                    line=dict(width=1.5, color="rgba(255,255,255,0.15)"),
                    symbol="circle",
                ),
                text=chart_df["mission"],
                hovertemplate="<b>%{text}</b><br>Payload: %{x:,} kg<br>Fuel: %{y:,} L<extra></extra>"
            ))
            fig1.update_layout(xaxis_title="Payload (kg)", yaxis_title="Fuel (L)")
            fig1 = styled_fig(fig1)
            st.plotly_chart(fig1, use_container_width=True, config={"displayModeBar": False})
            st.markdown('</div>', unsafe_allow_html=True)

        with cc2:
            st.markdown('<div style="margin:0 32px 0 16px;">', unsafe_allow_html=True)
            st.markdown("""
            <div class="chart-label">Chart 02 · Mission Cost: Success vs Failure</div>
            <div class="chart-hint">💡 Cost doesn't guarantee mission success</div>
            """, unsafe_allow_html=True)
            s_avg = success_df["cost"].mean() if len(success_df) > 0 else 0
            f_avg = fail_df["cost"].mean() if len(fail_df) > 0 else 0
            fig2 = go.Figure()
            fig2.add_trace(go.Bar(
                x=["Successful", "Failed"],
                y=[s_avg, f_avg],
                marker_color=["rgba(0,200,255,0.8)", "rgba(255,60,80,0.8)"],
                marker_line_width=0,
                hovertemplate="%{x}: $%{y:.1f}M<extra></extra>"
            ))
            fig2.update_layout(yaxis_title="Avg. Cost ($M)", showlegend=False, bargap=0.5)
            fig2 = styled_fig(fig2)
            st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
            st.markdown('</div>', unsafe_allow_html=True)

        cc3, cc4 = st.columns(2)

        with cc3:
            st.markdown('<div style="margin:0 16px 0 32px;">', unsafe_allow_html=True)
            st.markdown("""
            <div class="chart-label">Chart 03 · Mission Duration vs Distance</div>
            <div class="chart-hint">💡 Farther missions take significantly longer</div>
            """, unsafe_allow_html=True)
            sorted_df = chart_df.sort_values("distance")
            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(
                x=sorted_df["mission"].str[:14],
                y=sorted_df["duration"],
                mode="lines+markers",
                line=dict(color="#5060ff", width=2.5),
                fill="tozeroy",
                fillcolor="rgba(60,80,255,0.08)",
                marker=dict(color="#00c8ff", size=7, line=dict(width=1, color="rgba(255,255,255,0.2)")),
                hovertemplate="%{x}<br>Duration: %{y} days<extra></extra>"
            ))
            fig3.update_layout(yaxis_title="Duration (days)")
            fig3.update_xaxes(tickangle=-30)
            fig3 = styled_fig(fig3)
            st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})
            st.markdown('</div>', unsafe_allow_html=True)

        with cc4:
            st.markdown('<div style="margin:0 32px 0 16px;">', unsafe_allow_html=True)
            st.markdown("""
            <div class="chart-label">Chart 04 · Crew Size vs Mission Success</div>
            <div class="chart-hint">💡 Crewed missions show higher success correlation</div>
            """, unsafe_allow_html=True)
            sc_avg = success_df["crew"].mean() if len(success_df) > 0 else 0
            fc_avg = fail_df["crew"].mean() if len(fail_df) > 0 else 0
            fig4 = go.Figure()
            fig4.add_trace(go.Bar(
                x=["Successful", "Failed"],
                y=[round(sc_avg, 1), round(fc_avg, 1)],
                marker_color=["rgba(0,200,255,0.8)", "rgba(255,60,80,0.8)"],
                marker_line_width=0,
                hovertemplate="%{x}: %{y:.1f} crew<extra></extra>"
            ))
            fig4.update_layout(yaxis_title="Avg Crew Size", showlegend=False, bargap=0.5)
            fig4 = styled_fig(fig4)
            st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin:0 32px;">', unsafe_allow_html=True)
        st.markdown("""
        <div class="chart-label">Chart 05 · Correlation Analysis — All Variables</div>
        <div class="chart-hint">💡 Positive values = strong positive relationship; negative = inverse relationship</div>
        """, unsafe_allow_html=True)

        def safe_corr(a, b):
            if len(a) < 2:
                return 0.0
            r = np.corrcoef(a.values, b.values)
            return float(r[0, 1]) if not np.isnan(r[0, 1]) else 0.0

        labels = ["Cost vs\nPayload", "Cost vs\nFuel", "Cost vs\nDuration", "Payload vs\nFuel", "Payload vs\nDuration", "Fuel vs\nDuration"]
        pairs = [
            (chart_df["cost"], chart_df["payload"]),
            (chart_df["cost"], chart_df["fuel"]),
            (chart_df["cost"], chart_df["duration"]),
            (chart_df["payload"], chart_df["fuel"]),
            (chart_df["payload"], chart_df["duration"]),
            (chart_df["fuel"], chart_df["duration"]),
        ]
        corr_vals = [round(safe_corr(a, b) * 100, 1) for a, b in pairs]
        bar_colors = [
            "rgba(0,200,255,0.85)" if v > 60
            else "rgba(80,100,255,0.8)" if v >= 0
            else "rgba(255,60,80,0.8)"
            for v in corr_vals
        ]

        fig5 = go.Figure()
        fig5.add_trace(go.Bar(
            x=labels,
            y=corr_vals,
            marker_color=bar_colors,
            marker_line_width=0,
            hovertemplate="%{x}: %{y:.1f}%<extra></extra>"
        ))
        fig5.update_layout(yaxis_title="Correlation Coefficient (%)", yaxis=dict(range=[-100, 100]), showlegend=False, height=300)
        fig5 = styled_fig(fig5, height=300)
        st.plotly_chart(fig5, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    # ─── TAB 4: SIMULATION ───────────────────────────────────────────────────
    with tab4:
        st.markdown("""
        <div class="progress-wrap">
            <div class="progress-track"><div class="progress-fill" style="width:100%"></div></div>
            <div class="progress-label">Stage 4 of 4 &nbsp;·&nbsp; 100% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">🚀 Stage 04</div>
            <div class="stage-title">Rocket Launch Simulation</div>
            <div class="stage-desc">Adjust physics parameters to model rocket motion using Newton's laws of motion</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">⚙️ Simulation Parameters</div>', unsafe_allow_html=True)

        sp1, sp2 = st.columns(2)
        with sp1:
            payload_val = st.slider("Payload Weight (kg)", min_value=1000, max_value=50000, value=5000, step=500, key="payload_sim")
            st.caption("Heavier payload → More fuel needed to reach same altitude")
            thrust_val = st.slider("Thrust Force (N)", min_value=1000000, max_value=15000000, value=8000000, step=100000, key="thrust_sim")
            st.caption("Higher thrust → Greater acceleration & altitude")
        with sp2:
            fuel_val = st.slider("Initial Fuel (L)", min_value=50000, max_value=500000, value=200000, step=5000, key="fuel_sim")
            st.caption("More fuel → Longer burn time & higher velocity")
            drag_val = st.slider("Drag Factor", min_value=0.00001, max_value=0.001, value=0.0001, step=0.00001, format="%.5f", key="drag_sim")
            st.caption("Higher drag → More air resistance slowing rocket")

        run_sim = st.button("🚀  LAUNCH SIMULATION", key="run_sim_btn")
        st.markdown('</div>', unsafe_allow_html=True)

        if run_sim or "sim_results" in st.session_state:
            if run_sim:
                dt = 0.1
                gravity = 9.81
                mass = 5000.0 + payload_val
                fuel_mass = float(fuel_val)
                velocity = 0.0
                altitude = 0.0
                time_data, altitude_data, velocity_data, accel_data = [], [], [], []

                for step in range(int(300 / dt)):
                    t = step * dt
                    drag_force = drag_val * velocity * abs(velocity)
                    thrust_force = thrust_val if fuel_mass > 0 else 0
                    gravity_force = mass * gravity
                    net_force = thrust_force - gravity_force - drag_force
                    acceleration = net_force / mass
                    velocity += acceleration * dt
                    altitude += velocity * dt
                    if fuel_mass > 0:
                        burn = thrust_val * dt / 1000
                        fuel_mass -= burn
                        mass -= burn
                    if altitude < 0:
                        altitude = 0.0
                        velocity = 0.0
                        break
                    time_data.append(round(t, 1))
                    altitude_data.append(round(altitude, 2))
                    velocity_data.append(round(velocity, 2))
                    accel_data.append(round(acceleration, 4))

                st.session_state.sim_results = {
                    "time": time_data,
                    "altitude": altitude_data,
                    "velocity": velocity_data,
                    "accel": accel_data,
                }

            res = st.session_state.sim_results
            time_arr = res["time"]
            alt_arr  = res["altitude"]
            vel_arr  = res["velocity"]
            acc_arr  = res["accel"]

            sm1, sm2, sm3, sm4 = st.columns(4)
            sm1.metric("Max Altitude", f"{max(alt_arr):,.0f} m")
            sm2.metric("Max Velocity", f"{max(vel_arr):,.0f} m/s")
            sm3.metric("Flight Time", f"{len(time_arr) * 0.1:.1f} s")
            sm4.metric("Peak Acceleration", f"{max(acc_arr):.1f} m/s²")

            step_s = max(1, len(time_arr) // 120)
            s_time = time_arr[::step_s]
            s_alt  = alt_arr[::step_s]
            s_vel  = vel_arr[::step_s]
            s_acc  = acc_arr[::step_s]

            sc1, sc2 = st.columns(2)
            with sc1:
                st.markdown('<div style="margin:0 16px 0 32px;">', unsafe_allow_html=True)
                st.markdown('<div class="chart-label">Altitude vs Time</div>', unsafe_allow_html=True)
                fa = go.Figure()
                fa.add_trace(go.Scatter(
                    x=s_time, y=s_alt,
                    mode="lines",
                    line=dict(color="#00c8ff", width=2.5),
                    fill="tozeroy",
                    fillcolor="rgba(0,180,255,0.07)",
                ))
                fa.update_layout(xaxis_title="Time (s)", yaxis_title="Altitude (m)")
                fa = styled_fig(fa)
                st.plotly_chart(fa, use_container_width=True, config={"displayModeBar": False})
                st.markdown('</div>', unsafe_allow_html=True)

            with sc2:
                st.markdown('<div style="margin:0 32px 0 16px;">', unsafe_allow_html=True)
                st.markdown('<div class="chart-label">Velocity vs Time</div>', unsafe_allow_html=True)
                fv = go.Figure()
                fv.add_trace(go.Scatter(
                    x=s_time, y=s_vel,
                    mode="lines",
                    line=dict(color="#8060ff", width=2.5),
                    fill="tozeroy",
                    fillcolor="rgba(100,60,255,0.07)",
                ))
                fv.update_layout(xaxis_title="Time (s)", yaxis_title="Velocity (m/s)")
                fv = styled_fig(fv)
                st.plotly_chart(fv, use_container_width=True, config={"displayModeBar": False})
                st.markdown('</div>', unsafe_allow_html=True)

            sc3, sc4 = st.columns(2)
            with sc3:
                st.markdown('<div style="margin:0 16px 0 32px;">', unsafe_allow_html=True)
                st.markdown('<div class="chart-label">Acceleration vs Time</div>', unsafe_allow_html=True)
                fa2 = go.Figure()
                fa2.add_trace(go.Scatter(
                    x=s_time, y=s_acc,
                    mode="lines",
                    line=dict(color="#00ff9d", width=2.5),
                    fill="tozeroy",
                    fillcolor="rgba(0,200,120,0.07)",
                ))
                fa2.update_layout(xaxis_title="Time (s)", yaxis_title="Acceleration (m/s²)")
                fa2 = styled_fig(fa2)
                st.plotly_chart(fa2, use_container_width=True, config={"displayModeBar": False})
                st.markdown('</div>', unsafe_allow_html=True)

            with sc4:
                st.markdown("""
                <div style="margin:0 32px 0 16px; padding:24px; background:rgba(0,40,130,0.12); border:1px solid rgba(0,100,200,0.2); border-radius:12px; height:100%;">
                    <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00c8ff; letter-spacing:2px; margin-bottom:18px;">SIMULATION NOTES</div>
                    <div style="font-size:13px; color:rgba(160,200,255,0.7); line-height:1.9;">
                        › Thrust force peaks at ignition<br>
                        › As fuel burns, mass decreases → acceleration rises<br>
                        › Drag force = drag_factor × velocity²<br>
                        › Peak velocity occurs at max thrust-to-weight<br>
                        › Altitude continues rising even after engine cutoff<br>
                        › Newton's 2nd law governs all motion: F = ma
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # ── Footer bar ────────────────────────────────────────────────────────────
    st.markdown('<hr>', unsafe_allow_html=True)
    fl, fr = st.columns([5, 1])
    with fl:
        st.markdown("""
        <div style="padding:8px 32px; font-family:'Share Tech Mono',monospace; font-size:11px; color:rgba(100,140,200,0.4);">
            AEROSPACE DATA INSIGHTS PLATFORM &nbsp;·&nbsp; SYS:NOMINAL &nbsp;·&nbsp; DATA_INTEGRITY:VERIFIED
        </div>
        """, unsafe_allow_html=True)
    with fr:
        if st.button("⏻  LOGOUT", key="logout_btn"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            if "sim_results" in st.session_state:
                del st.session_state["sim_results"]
            st.rerun()