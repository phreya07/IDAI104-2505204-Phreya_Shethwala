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

/* ── Crypto insight cards ───────────────────────────────── */
.insight-card {
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 10px;
    font-size: 14px;
    font-family: 'Rajdhani', sans-serif;
    display: flex;
    align-items: center;
    gap: 12px;
}

.report-box {
    background: rgba(4, 12, 35, 0.85);
    border: 1px solid rgba(0, 140, 255, 0.25);
    border-radius: 14px;
    padding: 28px 32px;
    margin: 0 32px 32px;
    position: relative;
    overflow: hidden;
}

.report-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(0, 200, 255, 0.6), rgba(120, 60, 255, 0.5), transparent);
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

    st.markdown("""
    <div class="login-hero">
        <div class="login-badge">&#128752;&nbsp; MISSION CONTROL SYSTEM &nbsp; v2.4</div>
        <div class="login-heading">AEROSPACE<br>DATA INSIGHTS</div>
        <div class="login-subheading">Advanced space mission analytics &amp; rocket simulation platform</div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 1.1, 1])
    with col_m:
        st.markdown("""
        <div class="login-card">
            <div class="login-logo-area">
                <div class="login-logo-icon">&#128640;</div>
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
                st.error("Please enter credentials to proceed")

        st.markdown('<div class="login-demo-note">DEMO MODE — Any credentials accepted</div>', unsafe_allow_html=True)


# ─── MAIN DASHBOARD ───────────────────────────────────────────────────────────
else:
    st.markdown(f"""
    <div class="top-nav">
        <div class="nav-brand">
            <div class="nav-icon">&#128752;</div>
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
                &#128100; &nbsp; {st.session_state.user_email}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "01  FUNDAMENTALS",
        "02  DATA ANALYSIS",
        "03  VISUALIZATIONS",
        "04  SIMULATION",
        "05  CRYPTO SIM",
    ])

    # ─── TAB 1: UNDERSTANDING ────────────────────────────────────────────────
    with tab1:
        st.markdown("""
        <div class="progress-wrap">
            <div class="progress-track"><div class="progress-fill" style="width:25%"></div></div>
            <div class="progress-label">Stage 1 of 4 &nbsp;&#183;&nbsp; 25% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">&#128218; Stage 01</div>
            <div class="stage-title">Understanding Rocket Dynamics</div>
            <div class="stage-desc">Master the fundamental physics governing rocket launches before analyzing real mission data</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">&#9889; Newton's Second Law of Motion</div>
            <p style="font-size:15px; color:rgba(180,210,255,0.75); line-height:1.9; margin-bottom:20px;">
                Rocket motion is governed by <strong style="color:#a0c8ff;">Newton's Second Law of Motion</strong>, which states:
            </p>
            <div class="formula-box" style="margin-bottom:20px;">
                <div class="formula-label">The Fundamental Principle</div>
                <div class="formula-main">Force = Mass x Acceleration</div>
            </div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.8; margin-bottom:20px;">
                This means that acceleration depends on the <strong style="color:#a0c8ff;">net force</strong> acting on the rocket divided by its <strong style="color:#a0c8ff;">mass</strong>. The mathematical expression for rocket acceleration is:
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">&#128208; Rocket Acceleration Equation</div>
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
                            <span style="color:rgba(160,196,255,0.6); margin:0 6px;">&#8722;</span>
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
                    <div style="font-size:13px; color:rgba(0,220,120,0.9); letter-spacing:1px; margin-bottom:8px;">&#9650; &nbsp; THRUST (T)</div>
                    <div style="font-size:11px; color:rgba(160,196,255,0.4); margin-bottom:4px;">pushes rocket upward</div>
                    <div style="width:3px; height:40px; background:linear-gradient(180deg,rgba(0,220,120,0.6),rgba(0,200,255,0.2)); margin:8px auto;"></div>
                    <div style="width:60px; height:60px; background:linear-gradient(135deg,rgba(0,100,255,0.2),rgba(60,40,200,0.3)); border:1px solid rgba(0,150,255,0.3); border-radius:8px; margin:0 auto; display:flex; align-items:center; justify-content:center;">
                        <span style="font-size:22px;">&#128640;</span>
                    </div>
                    <div style="width:3px; height:40px; background:linear-gradient(180deg,rgba(255,80,80,0.2),rgba(255,60,60,0.6)); margin:8px auto;"></div>
                    <div style="font-size:11px; color:rgba(160,196,255,0.4); margin-bottom:4px;">pulls rocket downward</div>
                    <div style="font-size:13px; color:rgba(255,100,100,0.9); letter-spacing:1px;">&#9660; &nbsp; GRAVITY (mg) + DRAG (D)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">&#128302; Three Primary Forces Acting on a Rocket</div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.7; margin-bottom:20px;">
                During launch, three fundamental forces determine a rocket's trajectory and performance:
            </p>
        </div>
        """, unsafe_allow_html=True)

        fc1, fc2, fc3 = st.columns(3)
        forces = [
            ("&#9650;", "THRUST", "#00cc80", "rgba(0,180,100,0.15)", "rgba(0,150,80,0.25)",
             "Produced by the rocket engine, it pushes the rocket <strong style='color:#80ffcc;'>upward</strong>. Generated by burning propellant and expelling hot gases at high velocity through the nozzle.",
             "1"),
            ("&#9660;", "GRAVITY", "#ff6060", "rgba(220,60,60,0.15)", "rgba(200,40,40,0.25)",
             "Pulls the rocket <strong style='color:#ffaaaa;'>downward</strong> toward Earth at a constant <strong style='color:#ffaaaa;'>9.81 m/s²</strong>. Must be continuously overcome by thrust to gain or maintain altitude.",
             "2"),
            ("&#9676;", "DRAG", "#ffaa40", "rgba(220,140,0,0.15)", "rgba(200,120,0,0.25)",
             "Air resistance that <strong style='color:#ffd080;'>opposes upward motion</strong>. Strongest near Earth, decreases at higher altitudes due to reduced air density. Becomes negligible above 80 km.",
             "3"),
        ]
        for col, (icon, title, color, bg, border_c, desc, num) in zip([fc1, fc2, fc3], forces):
            with col:
                st.markdown(f"""
                <div style="background:{bg}; border:1px solid {border_c}; border-radius:14px; padding:24px 20px; text-align:center; height:100%;">
                    <div style="width:36px; height:36px; background:{border_c}; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; font-family:'Orbitron',monospace; font-size:13px; font-weight:700; color:{color}; margin-bottom:14px;">{num}</div>
                    <div style="font-size:32px; margin-bottom:10px;">{icon}</div>
                    <div style="font-family:'Orbitron',monospace; font-size:13px; font-weight:700; color:{color}; letter-spacing:2px; margin-bottom:12px;">{title}</div>
                    <div style="font-size:13px; color:rgba(180,210,255,0.65); line-height:1.7;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-top:24px;">
            <div class="card-title">&#127744; Drag Force Equation</div>
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
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; font-size:26px; color:#00cc80; margin-left:4px;">&#961;</span>
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
                        <span style="font-family:'Georgia','Times New Roman',serif; font-style:italic; color:#00cc80; font-size:17px;">&#961;</span>
                        <div style="font-size:12px; color:rgba(160,196,255,0.6); margin-top:4px;">Air density (kg/m&#179;)</div>
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
                    &#8250; As altitude increases, air density (&#961;) decreases &#8594; drag force reduces significantly
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">&#128293; Fuel Consumption &amp; Mass Reduction</div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.8; margin-bottom:16px;">
                As fuel burns, the rocket's <strong style="color:#a0c8ff;">total mass decreases continuously</strong>. Since acceleration equals
                force divided by mass (<span style="font-family:'Share Tech Mono',monospace; color:#00c8ff;">a = F/m</span>),
                a lower mass results in <strong style="color:#a0c8ff;">higher acceleration</strong> even with the same thrust force.
                This explains why rockets <em style="color:#80c8ff;">accelerate faster as fuel is consumed</em> — the engine output stays
                constant while the rocket grows lighter.
            </p>
            <div style="display:flex; gap:16px; flex-wrap:wrap;">
                <div style="flex:1; min-width:180px; background:rgba(0,50,150,0.12); border:1px solid rgba(0,100,200,0.2); border-radius:10px; padding:16px 18px; text-align:center;">
                    <div style="font-family:'Share Tech Mono',monospace; font-size:22px; color:#00c8ff; margin-bottom:6px;">m &#8595;</div>
                    <div style="font-size:12px; color:rgba(160,196,255,0.55);">Mass decreases<br>as fuel burns</div>
                </div>
                <div style="display:flex; align-items:center; font-size:22px; color:rgba(100,160,255,0.4);">&#8594;</div>
                <div style="flex:1; min-width:180px; background:rgba(0,50,150,0.12); border:1px solid rgba(0,100,200,0.2); border-radius:10px; padding:16px 18px; text-align:center;">
                    <div style="font-family:'Share Tech Mono',monospace; font-size:22px; color:#80a0ff; margin-bottom:6px;">F = const</div>
                    <div style="font-size:12px; color:rgba(160,196,255,0.55);">Thrust force<br>remains steady</div>
                </div>
                <div style="display:flex; align-items:center; font-size:22px; color:rgba(100,160,255,0.4);">&#8594;</div>
                <div style="flex:1; min-width:180px; background:rgba(0,180,100,0.08); border:1px solid rgba(0,180,100,0.2); border-radius:10px; padding:16px 18px; text-align:center;">
                    <div style="font-family:'Share Tech Mono',monospace; font-size:22px; color:#00cc80; margin-bottom:6px;">a &#8593;&#8593;</div>
                    <div style="font-size:12px; color:rgba(160,196,255,0.55);">Acceleration<br>increases!</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">&#128279; Connection to Dataset</div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.8; margin-bottom:20px;">
                The provided mission dataset contains real-world variables that directly reflect these physics principles:
            </p>
        </div>
        """, unsafe_allow_html=True)

        ds1, ds2 = st.columns(2)
        dataset_vars = [
            ("&#128230;", "Payload Weight", "Directly affects total mass — higher payload increases required thrust and fuel consumption"),
            ("&#9981;", "Fuel Consumption", "Tied to payload weight, mission distance, and thrust requirements"),
            ("&#128176;", "Mission Cost", "Often related to fuel usage, vehicle complexity, and mission distance"),
            ("&#9203;", "Mission Duration", "Influenced by distance from Earth and propulsion efficiency"),
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
                &#8250; <strong style="color:#a0c8ff;">Mission success</strong> may depend on the optimal balance between thrust, fuel capacity, and payload weight — confirming that physics governs real-world outcomes.
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-top:24px;">
            <div class="card-title">&#10067; Guiding Questions</div>
        """, unsafe_allow_html=True)

        guiding = [
            ("Q1", "How does adding more payload affect altitude?",
             "Increasing payload increases mass, which reduces acceleration. More thrust and fuel are required to reach higher altitudes. The relationship is directly governed by a = F/m."),
            ("Q2", "How does increasing thrust affect launch success?",
             "Higher thrust increases net force, improving acceleration and the ability to overcome gravity quickly. This directly correlates with higher success rates in our dataset."),
            ("Q3", "Does lower drag at higher altitudes improve speed?",
             "Yes — reduced air density decreases drag force (Drag = 1/2 x Cd x rho x A x v^2), allowing the rocket to move more efficiently. This is why rockets gain speed rapidly above 50 km."),
            ("Q4", "Can simulation values be compared to real mission data?",
             "Yes. Trends observed in simulation — such as higher payload requiring more fuel — can be directly validated using real-world dataset patterns in Stages 2 and 3."),
        ]
        for tag, q, a in guiding:
            st.markdown(f"""
            <div class="qa-card">
                <div class="qa-question">[{tag}] &nbsp; {q}</div>
                <div class="qa-answer"><span class="qa-check">&#8250;</span>{a}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin:0 32px 32px; background:linear-gradient(135deg, rgba(0,60,200,0.12), rgba(40,0,160,0.1)); border:1px solid rgba(0,120,255,0.2); border-radius:14px; padding:28px 32px; position:relative; overflow:hidden;">
            <div style="position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg, transparent, rgba(0,180,255,0.5), rgba(100,60,255,0.5), transparent);"></div>
            <div style="font-family:'Orbitron',monospace; font-size:12px; font-weight:700; color:#00c8ff; letter-spacing:2px; text-transform:uppercase; margin-bottom:14px;">&#127757; Real-World Importance</div>
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
            <div class="progress-label">Stage 2 of 4 &nbsp;&#183;&nbsp; 50% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">&#128202; Stage 02</div>
            <div class="stage-title">Data Preprocessing &amp; Cleaning</div>
            <div class="stage-desc">The dataset was carefully examined and cleaned to ensure accuracy and reliability before analysis</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Compact 5-step pipeline ───────────────────────────────────────────
        st.markdown("""
        <div style="margin:0 32px 20px; display:grid; grid-template-columns:repeat(5,1fr); gap:10px;">
          <div style="background:rgba(0,30,80,0.5);border:1px solid rgba(0,200,255,0.2);border-top:3px solid #00c8ff;border-radius:10px;padding:16px 14px;text-align:center;">
            <div style="font-size:22px;font-weight:900;color:#00c8ff;opacity:0.2;margin-bottom:6px;font-family:monospace;">01</div>
            <div style="font-size:10px;font-weight:700;color:#00c8ff;letter-spacing:1px;margin-bottom:10px;font-family:sans-serif;">LOAD</div>
            <div style="font-size:10px;color:rgba(0,200,255,0.7);background:rgba(0,200,255,0.07);border-radius:4px;padding:5px;margin-bottom:8px;font-family:monospace;">pd.read_csv()</div>
            <div style="font-size:11px;color:rgba(160,196,255,0.55);line-height:1.5;">Inspect with head(), info(), describe()</div>
          </div>
          <div style="background:rgba(0,30,80,0.5);border:1px solid rgba(128,160,255,0.2);border-top:3px solid #80a0ff;border-radius:10px;padding:16px 14px;text-align:center;">
            <div style="font-size:22px;font-weight:900;color:#80a0ff;opacity:0.2;margin-bottom:6px;font-family:monospace;">02</div>
            <div style="font-size:10px;font-weight:700;color:#80a0ff;letter-spacing:1px;margin-bottom:10px;font-family:sans-serif;">TYPES</div>
            <div style="font-size:10px;color:rgba(128,160,255,0.7);background:rgba(128,160,255,0.07);border-radius:4px;padding:5px;margin-bottom:8px;font-family:monospace;">to_datetime()</div>
            <div style="font-size:11px;color:rgba(160,196,255,0.55);line-height:1.5;">Convert dates and numerics, coerce errors</div>
          </div>
          <div style="background:rgba(0,30,80,0.5);border:1px solid rgba(255,170,64,0.2);border-top:3px solid #ffaa40;border-radius:10px;padding:16px 14px;text-align:center;">
            <div style="font-size:22px;font-weight:900;color:#ffaa40;opacity:0.2;margin-bottom:6px;font-family:monospace;">03</div>
            <div style="font-size:10px;font-weight:700;color:#ffaa40;letter-spacing:1px;margin-bottom:10px;font-family:sans-serif;">NULLS</div>
            <div style="font-size:10px;color:rgba(255,170,64,0.7);background:rgba(255,170,64,0.07);border-radius:4px;padding:5px;margin-bottom:8px;font-family:monospace;">fillna(median)</div>
            <div style="font-size:11px;color:rgba(160,196,255,0.55);line-height:1.5;">Drop critical nulls, fill gaps with median</div>
          </div>
          <div style="background:rgba(0,30,80,0.5);border:1px solid rgba(255,96,128,0.2);border-top:3px solid #ff6080;border-radius:10px;padding:16px 14px;text-align:center;">
            <div style="font-size:22px;font-weight:900;color:#ff6080;opacity:0.2;margin-bottom:6px;font-family:monospace;">04</div>
            <div style="font-size:10px;font-weight:700;color:#ff6080;letter-spacing:1px;margin-bottom:10px;font-family:sans-serif;">DEDUPE</div>
            <div style="font-size:10px;color:rgba(255,96,128,0.7);background:rgba(255,96,128,0.07);border-radius:4px;padding:5px;margin-bottom:8px;font-family:monospace;">drop_duplicates()</div>
            <div style="font-size:11px;color:rgba(160,196,255,0.55);line-height:1.5;">Remove duplicates, reset index to 0</div>
          </div>
          <div style="background:rgba(0,30,80,0.5);border:1px solid rgba(0,204,128,0.2);border-top:3px solid #00cc80;border-radius:10px;padding:16px 14px;text-align:center;">
            <div style="font-size:22px;font-weight:900;color:#00cc80;opacity:0.2;margin-bottom:6px;font-family:monospace;">05</div>
            <div style="font-size:10px;font-weight:700;color:#00cc80;letter-spacing:1px;margin-bottom:10px;font-family:sans-serif;">ENRICH</div>
            <div style="font-size:10px;color:rgba(0,204,128,0.7);background:rgba(0,204,128,0.07);border-radius:4px;padding:5px;margin-bottom:8px;font-family:monospace;">.dt.year</div>
            <div style="font-size:11px;color:rgba(160,196,255,0.55);line-height:1.5;">Extract year column for filter and analysis</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin:24px 32px 0; border-top:1px solid rgba(0,80,200,0.15); padding-top:24px;">
            <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00a8ff; letter-spacing:2px; margin-bottom:16px;">&#128203; CLEANED DATASET — LIVE PREVIEW</div>
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
            <div class="progress-label">Stage 3 of 4 &nbsp;&#183;&nbsp; 75% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">&#128200; Stage 03</div>
            <div class="stage-title">Interactive Visualizations</div>
            <div class="stage-desc">Analyze relationships between rocket characteristics and mission outcomes across 5 charts</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">&#128302; Chart Filter</div>', unsafe_allow_html=True)
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
            <div class="chart-hint">Heavier payload = More fuel required</div>
            """, unsafe_allow_html=True)
            colors = ["#00c8ff" if s == "Yes" else "#ff4466" for s in chart_df["success"]]
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(
                x=chart_df["payload"], y=chart_df["fuel"],
                mode="markers",
                marker=dict(color=colors, size=11, line=dict(width=1.5, color="rgba(255,255,255,0.15)"), symbol="circle"),
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
            <div class="chart-hint">Cost does not guarantee mission success</div>
            """, unsafe_allow_html=True)
            s_avg = success_df["cost"].mean() if len(success_df) > 0 else 0
            f_avg = fail_df["cost"].mean() if len(fail_df) > 0 else 0
            fig2 = go.Figure()
            fig2.add_trace(go.Bar(
                x=["Successful", "Failed"], y=[s_avg, f_avg],
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
            <div class="chart-hint">Farther missions take significantly longer</div>
            """, unsafe_allow_html=True)
            sorted_df = chart_df.sort_values("distance")
            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(
                x=sorted_df["mission"].str[:14], y=sorted_df["duration"],
                mode="lines+markers",
                line=dict(color="#5060ff", width=2.5),
                fill="tozeroy", fillcolor="rgba(60,80,255,0.08)",
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
            <div class="chart-hint">Crewed missions show higher success correlation</div>
            """, unsafe_allow_html=True)
            sc_avg = success_df["crew"].mean() if len(success_df) > 0 else 0
            fc_avg = fail_df["crew"].mean() if len(fail_df) > 0 else 0
            fig4 = go.Figure()
            fig4.add_trace(go.Bar(
                x=["Successful", "Failed"], y=[round(sc_avg, 1), round(fc_avg, 1)],
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
        <div class="chart-hint">Positive values = strong positive relationship; negative = inverse relationship</div>
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
            x=labels, y=corr_vals,
            marker_color=bar_colors, marker_line_width=0,
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
            <div class="progress-label">Stage 4 of 4 &nbsp;&#183;&nbsp; 100% Complete</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">&#128640; Stage 04</div>
            <div class="stage-title">Rocket Launch Simulation</div>
            <div class="stage-desc">Adjust physics parameters to model rocket motion using Newton's laws of motion</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card-title">&#9881; Simulation Parameters</div>', unsafe_allow_html=True)

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

        run_sim = st.button("LAUNCH SIMULATION", key="run_sim_btn")

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
                    "time": time_data, "altitude": altitude_data,
                    "velocity": velocity_data, "accel": accel_data,
                }

            res = st.session_state.sim_results
            time_arr = res["time"]; alt_arr = res["altitude"]
            vel_arr = res["velocity"]; acc_arr = res["accel"]

            sm1, sm2, sm3, sm4 = st.columns(4)
            sm1.metric("Max Altitude", f"{max(alt_arr):,.0f} m")
            sm2.metric("Max Velocity", f"{max(vel_arr):,.0f} m/s")
            sm3.metric("Flight Time", f"{len(time_arr) * 0.1:.1f} s")
            sm4.metric("Peak Acceleration", f"{max(acc_arr):.1f} m/s²")

            step_s = max(1, len(time_arr) // 120)
            s_time = time_arr[::step_s]; s_alt = alt_arr[::step_s]
            s_vel = vel_arr[::step_s]; s_acc = acc_arr[::step_s]

            sc1, sc2 = st.columns(2)
            with sc1:
                st.markdown('<div style="margin:0 16px 0 32px;">', unsafe_allow_html=True)
                st.markdown('<div class="chart-label">Altitude vs Time</div>', unsafe_allow_html=True)
                fa = go.Figure()
                fa.add_trace(go.Scatter(x=s_time, y=s_alt, mode="lines", line=dict(color="#00c8ff", width=2.5), fill="tozeroy", fillcolor="rgba(0,180,255,0.07)"))
                fa.update_layout(xaxis_title="Time (s)", yaxis_title="Altitude (m)")
                fa = styled_fig(fa)
                st.plotly_chart(fa, use_container_width=True, config={"displayModeBar": False})
                st.markdown('</div>', unsafe_allow_html=True)

            with sc2:
                st.markdown('<div style="margin:0 32px 0 16px;">', unsafe_allow_html=True)
                st.markdown('<div class="chart-label">Velocity vs Time</div>', unsafe_allow_html=True)
                fv = go.Figure()
                fv.add_trace(go.Scatter(x=s_time, y=s_vel, mode="lines", line=dict(color="#8060ff", width=2.5), fill="tozeroy", fillcolor="rgba(100,60,255,0.07)"))
                fv.update_layout(xaxis_title="Time (s)", yaxis_title="Velocity (m/s)")
                fv = styled_fig(fv)
                st.plotly_chart(fv, use_container_width=True, config={"displayModeBar": False})
                st.markdown('</div>', unsafe_allow_html=True)

            sc3, sc4 = st.columns(2)
            with sc3:
                st.markdown('<div style="margin:0 16px 0 32px;">', unsafe_allow_html=True)
                st.markdown('<div class="chart-label">Acceleration vs Time</div>', unsafe_allow_html=True)
                fa2 = go.Figure()
                fa2.add_trace(go.Scatter(x=s_time, y=s_acc, mode="lines", line=dict(color="#00ff9d", width=2.5), fill="tozeroy", fillcolor="rgba(0,200,120,0.07)"))
                fa2.update_layout(xaxis_title="Time (s)", yaxis_title="Acceleration (m/s²)")
                fa2 = styled_fig(fa2)
                st.plotly_chart(fa2, use_container_width=True, config={"displayModeBar": False})
                st.markdown('</div>', unsafe_allow_html=True)

            with sc4:
                st.markdown("""
                <div style="margin:0 32px 0 16px; padding:24px; background:rgba(0,40,130,0.12); border:1px solid rgba(0,100,200,0.2); border-radius:12px; height:100%;">
                    <div style="font-family:'Orbitron',monospace; font-size:11px; color:#00c8ff; letter-spacing:2px; margin-bottom:18px;">SIMULATION NOTES</div>
                    <div style="font-size:13px; color:rgba(160,200,255,0.7); line-height:1.9;">
                        &#8250; Thrust force peaks at ignition<br>
                        &#8250; As fuel burns, mass decreases &#8594; acceleration rises<br>
                        &#8250; Drag force = drag_factor &#215; velocity&#178;<br>
                        &#8250; Peak velocity occurs at max thrust-to-weight<br>
                        &#8250; Altitude continues rising even after engine cutoff<br>
                        &#8250; Newton's 2nd law governs all motion: F = ma
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # ─── TAB 5: CRYPTO SIM ───────────────────────────────────────────────────
    with tab5:
        st.markdown("""
        <div class="progress-wrap">
            <div class="progress-track"><div class="progress-fill" style="width:100%"></div></div>
            <div class="progress-label">Bonus Module &nbsp;&#183;&nbsp; Cryptocurrency Market Simulation</div>
        </div>
        <div class="stage-header">
            <div class="stage-tag">&#8383; Bonus Module</div>
            <div class="stage-title">Cryptocurrency Price Simulation</div>
            <div class="stage-desc">Generate synthetic crypto price data using NumPy mathematical models · Analyze volatility · Compare asset types</div>
        </div>
        """, unsafe_allow_html=True)

        # ── SECTION 1: Data Generation Parameters ────────────────────────────
        st.markdown("""
        <div class="card">
            <div class="card-title">&#9881; Section 1 — Data Generation Parameters (NumPy)</div>
            <p style="font-size:14px; color:rgba(160,196,255,0.65); line-height:1.8; margin-bottom:4px;">
                Synthetic price data is generated using the formula:<br>
                <span style="font-family:'Share Tech Mono',monospace; color:#00c8ff; font-size:15px;">
                    Price = Amplitude x sin(Frequency x Time) + Drift x Time + Noise
                </span>
            </p>
        </div>
        """, unsafe_allow_html=True)

        cp1, cp2 = st.columns(2)
        with cp1:
            c_time_steps = st.slider("Time Steps (Trading Periods)", min_value=50, max_value=500, value=200, step=10, key="c_time")
            st.caption("Number of simulated trading periods")
            c_amplitude = st.slider("Amplitude", min_value=1.0, max_value=50.0, value=10.0, step=0.5, key="c_amp")
            st.caption("Controls the height of price swings")
            c_frequency = st.slider("Frequency", min_value=0.01, max_value=1.0, value=0.1, step=0.01, key="c_freq")
            st.caption("Controls how rapidly price oscillates")
        with cp2:
            c_drift = st.slider("Drift", min_value=-2.0, max_value=2.0, value=0.05, step=0.01, key="c_drift")
            st.caption("Positive = upward trend · Negative = downward trend")
            c_noise = st.slider("Noise Level", min_value=0.0, max_value=20.0, value=3.0, step=0.5, key="c_noise")
            st.caption("Higher noise = more unpredictable price movement")
            c_base_price = st.slider("Base Price ($)", min_value=100, max_value=50000, value=1000, step=100, key="c_base")
            st.caption("Starting price of the simulated asset")

        # ── Generate data ─────────────────────────────────────────────────────
        np.random.seed(42)
        time_arr_c = np.arange(c_time_steps)
        sine_component = c_amplitude * np.sin(c_frequency * time_arr_c)
        drift_component = c_drift * time_arr_c
        noise_component = np.random.normal(0, c_noise, c_time_steps)
        price_arr = c_base_price + sine_component + drift_component + noise_component

        # ── Store in DataFrame ────────────────────────────────────────────────
        crypto_df = pd.DataFrame({
            "Time":             time_arr_c,
            "Price":            price_arr,
            "Drift_Component":  drift_component,
            "Noise_Component":  noise_component,
        })

        # ── SECTION 2: DataFrame Preview ─────────────────────────────────────
        st.markdown("""
        <div class="card">
            <div class="card-title">&#128203; Section 2 — Pandas DataFrame Preview</div>
            <p style="font-size:13px; color:rgba(160,196,255,0.6); line-height:1.8; margin-bottom:16px;">
                The generated data is stored in a Pandas DataFrame. Below are the first 5 rows (<code style="color:#00c8ff;">.head()</code>):
            </p>
        </div>
        """, unsafe_allow_html=True)

        head_df = crypto_df.head()
        head_rows = ""
        for _, row in head_df.iterrows():
            head_rows += (
                '<tr class="data-row">'
                '<td style="font-family:Share Tech Mono,monospace;color:#00c8ff;">' + str(int(row['Time'])) + '</td>'
                '<td style="font-family:Share Tech Mono,monospace;color:#c8d8f0;">$' + f"{row['Price']:.2f}" + '</td>'
                '<td style="font-family:Share Tech Mono,monospace;color:#80a0ff;">' + f"{row['Drift_Component']:.4f}" + '</td>'
                '<td style="font-family:Share Tech Mono,monospace;color:#ffaa40;">' + f"{row['Noise_Component']:.4f}" + '</td>'
                '</tr>'
            )
        head_table = (
            '<div class="custom-table-wrap">'
            '<table class="custom-table"><thead><tr>'
            '<th>Time</th><th>Price ($)</th><th>Drift Component</th><th>Noise Component</th>'
            '</tr></thead><tbody>' + head_rows + '</tbody></table></div>'
        )
        st.markdown(head_table, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin:12px 32px 24px; display:grid; grid-template-columns:1fr 1fr; gap:12px;">
            <div style="background:rgba(0,40,130,0.15); border:1px solid rgba(0,100,200,0.2); border-left:3px solid #00c8ff; border-radius:8px; padding:12px 16px;">
                <div style="font-family:'Orbitron',monospace; font-size:10px; color:#00c8ff; letter-spacing:1.5px; margin-bottom:6px;">TIME</div>
                <div style="font-size:13px; color:rgba(160,196,255,0.7);">Represents simulated trading period (0, 1, 2 ... N). Each unit equals one trading interval (e.g., one hour or one day).</div>
            </div>
            <div style="background:rgba(0,40,130,0.15); border:1px solid rgba(0,100,200,0.2); border-left:3px solid #80a0ff; border-radius:8px; padding:12px 16px;">
                <div style="font-family:'Orbitron',monospace; font-size:10px; color:#80a0ff; letter-spacing:1.5px; margin-bottom:6px;">PRICE</div>
                <div style="font-size:13px; color:rgba(160,196,255,0.7);">Final simulated asset price. Combines the sine wave, drift trend, and random noise components.</div>
            </div>
            <div style="background:rgba(0,40,130,0.15); border:1px solid rgba(0,100,200,0.2); border-left:3px solid #5060ff; border-radius:8px; padding:12px 16px;">
                <div style="font-family:'Orbitron',monospace; font-size:10px; color:#5060ff; letter-spacing:1.5px; margin-bottom:6px;">DRIFT COMPONENT</div>
                <div style="font-size:13px; color:rgba(160,196,255,0.7);">Long-term trend component (Drift x Time). Positive drift = bullish trend; negative = bearish.</div>
            </div>
            <div style="background:rgba(0,40,130,0.15); border:1px solid rgba(0,100,200,0.2); border-left:3px solid #ffaa40; border-radius:8px; padding:12px 16px;">
                <div style="font-family:'Orbitron',monospace; font-size:10px; color:#ffaa40; letter-spacing:1.5px; margin-bottom:6px;">NOISE COMPONENT</div>
                <div style="font-size:13px; color:rgba(160,196,255,0.7);">Random market fluctuations drawn from a normal distribution. Simulates unpredictable market events.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── NOTE: Section 3 (Data Cleaning) has been removed ─────────────────

        # ── Compute stats with NumPy/Pandas ───────────────────────────────────
        crypto_df_clean = crypto_df.copy()
        crypto_df_clean = crypto_df_clean[crypto_df_clean["Price"] > 0].reset_index(drop=True)
        crypto_df_clean["Time"] = crypto_df_clean["Time"].astype(int)
        crypto_df_clean["Price"] = crypto_df_clean["Price"].astype(float)
        crypto_df_clean["Drift_Component"] = crypto_df_clean["Drift_Component"].astype(float)
        crypto_df_clean["Noise_Component"] = crypto_df_clean["Noise_Component"].astype(float)

        prices = crypto_df_clean["Price"].values
        mean_price   = float(np.mean(prices))
        std_price    = float(np.std(prices))
        var_price    = float(np.var(prices))
        returns      = np.diff(prices) / prices[:-1]
        mean_return  = float(np.mean(returns)) * 100

        # Volatility classification
        if std_price < 5:
            vol_level = "LOW"
            vol_color = "#00cc80"
            vol_bg    = "rgba(0,180,100,0.12)"
            vol_border= "rgba(0,160,80,0.3)"
            vol_icon  = "LOW"
            vol_desc  = "Standard deviation below 5 indicates stable, predictable price movement with minimal risk."
        elif std_price < 15:
            vol_level = "MEDIUM"
            vol_color = "#ffaa40"
            vol_bg    = "rgba(220,140,0,0.12)"
            vol_border= "rgba(200,120,0,0.3)"
            vol_icon  = "MED"
            vol_desc  = "Standard deviation between 5 and 15 reflects moderate fluctuation typical of mid-cap crypto assets."
        else:
            vol_level = "HIGH"
            vol_color = "#ff4466"
            vol_bg    = "rgba(255,60,80,0.12)"
            vol_border= "rgba(220,40,60,0.3)"
            vol_icon  = "HIGH"
            vol_desc  = "Standard deviation above 15 signals highly unpredictable price behavior — significant risk involved."

        # ── SECTION 3 (renumbered): Volatility & Statistics ───────────────────
        st.markdown("""
        <div class="card">
            <div class="card-title">&#128202; Section 3 — Statistical Analysis &amp; Volatility Classification</div>
            <p style="font-size:13px; color:rgba(160,196,255,0.55); margin-bottom:20px;">
                All metrics computed using <code style="color:#00c8ff;">NumPy</code> and <code style="color:#00c8ff;">Pandas</code> on the cleaned price array.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # 4 stat metric cards
        stat1, stat2, stat3, stat4 = st.columns(4)
        stat1.metric("Mean Price", f"${mean_price:,.2f}")
        stat2.metric("Std Deviation (s)", f"{std_price:.4f}")
        stat3.metric("Variance (s2)", f"{var_price:.4f}")
        stat4.metric("Mean Return", f"{mean_return:.4f}%")

        # Volatility classification banner
        st.markdown(f"""
        <div style="margin:20px 32px 8px; background:{vol_bg}; border:1px solid {vol_border}; border-radius:16px; padding:24px 28px; display:flex; align-items:center; gap:24px; position:relative; overflow:hidden;">
            <div style="position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg, transparent, {vol_color}80, transparent);"></div>
            <div style="width:70px; height:70px; background:{vol_bg}; border:2px solid {vol_color}60; border-radius:50%; display:flex; align-items:center; justify-content:center; font-family:'Orbitron',monospace; font-size:13px; font-weight:900; color:{vol_color}; flex-shrink:0; letter-spacing:1px;">
                {vol_icon}
            </div>
            <div style="flex:1;">
                <div style="font-family:'Share Tech Mono',monospace; font-size:10px; color:rgba(160,196,255,0.45); letter-spacing:3px; margin-bottom:6px;">VOLATILITY CLASSIFICATION · s = {std_price:.4f}</div>
                <div style="font-family:'Orbitron',monospace; font-size:26px; font-weight:900; color:{vol_color}; letter-spacing:4px; margin-bottom:8px;">{vol_level} VOLATILITY</div>
                <div style="font-size:13px; color:rgba(180,210,255,0.65); line-height:1.6;">{vol_desc}</div>
            </div>
            <div style="text-align:right; flex-shrink:0;">
                <div style="font-family:'Share Tech Mono',monospace; font-size:11px; color:rgba(160,196,255,0.4); margin-bottom:4px;">THRESHOLD</div>
                <div style="font-family:'Share Tech Mono',monospace; font-size:13px; color:rgba(160,196,255,0.65); line-height:1.8;">
                    s &lt; 5 &#8594; LOW<br>
                    5 &#8804; s &lt; 15 &#8594; MEDIUM<br>
                    s &#8805; 15 &#8594; HIGH
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── SECTION 4 (renumbered): Interactive Price Visualization ──────────
        st.markdown("""
        <div class="card" style="margin-top:24px;">
            <div class="card-title">&#128200; Section 4 — Interactive Price Visualization</div>
        </div>
        """, unsafe_allow_html=True)

        compare_mode = st.selectbox(
            "Comparison Mode",
            ["Single Asset", "Stable vs Volatile Asset Comparison"],
            key="c_compare"
        )

        st.markdown('<div style="margin:0 32px;">', unsafe_allow_html=True)

        if compare_mode == "Single Asset":
            st.markdown('<div class="chart-label">Cryptocurrency Price vs Time</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-hint">Blue line = simulated price · Fill shows price area under curve</div>', unsafe_allow_html=True)

            fig_c = go.Figure()
            fig_c.add_trace(go.Scatter(
                x=crypto_df_clean["Time"],
                y=crypto_df_clean["Price"],
                mode="lines",
                name="Price",
                line=dict(color="#00c8ff", width=2),
                fill="tozeroy",
                fillcolor="rgba(0,180,255,0.06)",
                hovertemplate="Time: %{x}<br>Price: $%{y:.2f}<extra></extra>"
            ))
            fig_c.update_layout(
                xaxis_title="Time (Trading Period)",
                yaxis_title="Price ($)",
                height=360,
            )
            fig_c = styled_fig(fig_c, height=360)
            st.plotly_chart(fig_c, use_container_width=True, config={"displayModeBar": False})

        else:
            st.markdown('<div class="chart-label">Stable Asset vs Volatile Asset — Price Comparison</div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-hint">Cyan = Stable (low amplitude, low noise) · Orange = Volatile (high amplitude, high noise)</div>', unsafe_allow_html=True)

            t_comp = np.arange(c_time_steps)
            stable_price   = c_base_price + (2  * np.sin(0.05 * t_comp)) + (0.01 * t_comp) + np.random.normal(0, 1,  c_time_steps)
            volatile_price = c_base_price + (30 * np.sin(0.3  * t_comp)) + (0.05 * t_comp) + np.random.normal(0, 12, c_time_steps)
            stable_price   = np.clip(stable_price,   1, None)
            volatile_price = np.clip(volatile_price, 1, None)

            fig_comp = go.Figure()
            fig_comp.add_trace(go.Scatter(
                x=t_comp, y=stable_price, mode="lines", name="Stable Asset",
                line=dict(color="#00c8ff", width=2),
                hovertemplate="Time: %{x}<br>Stable: $%{y:.2f}<extra></extra>"
            ))
            fig_comp.add_trace(go.Scatter(
                x=t_comp, y=volatile_price, mode="lines", name="Volatile Asset",
                line=dict(color="#ffaa40", width=2),
                hovertemplate="Time: %{x}<br>Volatile: $%{y:.2f}<extra></extra>"
            ))
            fig_comp.update_layout(
                xaxis_title="Time (Trading Period)",
                yaxis_title="Price ($)",
                height=360,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            fig_comp = styled_fig(fig_comp, height=360)
            st.plotly_chart(fig_comp, use_container_width=True, config={"displayModeBar": False})

        st.markdown('</div>', unsafe_allow_html=True)

        # ── Market Signal Badges ─────────────────────────────────────────────
        signals = []
        if c_amplitude > 10:
            signals.append(("HIGH VOL","#ff4466","rgba(255,40,70,0.12)","rgba(255,60,80,0.3)",
                "High Volatility Detected", f"Amplitude {c_amplitude} exceeds 10 — wide price swings, high-risk asset."))
        else:
            signals.append(("STABLE","#00cc80","rgba(0,180,100,0.12)","rgba(0,160,80,0.3)",
                "Stable Asset Detected", f"Amplitude {c_amplitude} is low — contained movement, conservative asset."))
        if c_drift > 0:
            signals.append(("BULL","#00cc80","rgba(0,180,100,0.12)","rgba(0,160,80,0.3)",
                "Bullish Trend", f"Positive drift +{c_drift:.2f} signals upward price momentum."))
        elif c_drift < 0:
            signals.append(("BEAR","#ff6060","rgba(255,60,60,0.12)","rgba(220,40,40,0.3)",
                "Bearish Trend", f"Negative drift {c_drift:.2f} signals downward price pressure."))
        else:
            signals.append(("FLAT","#80a0ff","rgba(80,100,255,0.12)","rgba(60,80,200,0.3)",
                "Neutral Trend", "Drift is 0 — purely cyclical movement."))
        if c_frequency > 0.5:
            signals.append(("FAST","#ffaa40","rgba(220,140,0,0.12)","rgba(200,120,0,0.3)",
                "Rapid Price Swings", f"Frequency {c_frequency:.2f} — fast oscillations, speculative asset."))
        elif c_frequency > 0.2:
            signals.append(("MID","#80a0ff","rgba(80,100,255,0.12)","rgba(60,80,200,0.3)",
                "Moderate Oscillation", f"Frequency {c_frequency:.2f} — moderate cyclical patterns."))
        else:
            signals.append(("SLOW","#60b0ff","rgba(40,100,220,0.12)","rgba(30,80,180,0.3)",
                "Slow Long-Term Cycles", f"Frequency {c_frequency:.2f} — gradual macro-driven cycles."))
        if c_noise > 10:
            signals.append(("NOISY","#ff8855","rgba(255,100,60,0.12)","rgba(220,80,40,0.3)",
                "High Unpredictability", f"Noise {c_noise} introduces major random fluctuations."))

        st.markdown('<div style="margin:8px 32px 4px;font-family:Orbitron,monospace;font-size:10px;color:rgba(0,200,255,0.5);letter-spacing:3px;">&#9658; MARKET SIGNAL ANALYSIS</div>', unsafe_allow_html=True)

        # Render badges in pairs using st.columns
        sig_pairs = [signals[i:i+2] for i in range(0, len(signals), 2)]
        for pair in sig_pairs:
            bcols = st.columns(len(pair))
            for ci, sig in enumerate(pair):
                ilabel, icolor, ibg, iborder, slabel, sdetail = sig
                with bcols[ci]:
                    badge_md = (
                        '<div style="background:' + ibg + ';border:1px solid ' + iborder +
                        ';border-left:4px solid ' + icolor + ';border-radius:12px;padding:14px 16px;'
                        'display:flex;align-items:flex-start;gap:12px;margin-bottom:10px;">'
                        '<div style="min-width:46px;height:46px;background:' + ibg +
                        ';border:1px solid ' + icolor + ';border-radius:8px;display:flex;'
                        'align-items:center;justify-content:center;font-family:monospace;'
                        'font-size:8px;font-weight:900;color:' + icolor + ';text-align:center;'
                        'line-height:1.2;flex-shrink:0;padding:3px;">' + ilabel + '</div>'
                        '<div><div style="font-size:11px;font-weight:700;color:' + icolor +
                        ';letter-spacing:1px;margin-bottom:4px;">' + slabel + '</div>'
                        '<div style="font-size:12px;color:rgba(200,220,255,0.7);line-height:1.5;">' + sdetail + '</div>'
                        '</div></div>'
                    )
                    st.markdown(badge_md, unsafe_allow_html=True)

        # ── Section 5: Flashcards via Plotly buttons (pure Streamlit) ─────────
        st.markdown("""
        <div class="card" style="margin-top:20px;">
            <div class="card-title">&#128269; Section 5 — Analytical Explanation</div>
            <p style="font-size:13px;color:rgba(160,196,255,0.5);margin:0;">
                Select a parameter below to learn how it shapes the crypto price simulation.
            </p>
        </div>
        """, unsafe_allow_html=True)

        fc_items = [
            ("01","#00c8ff","Amplitude","Controls the peak-to-trough range of the sine wave. Higher amplitude = dramatic swings (volatile). Lower amplitude = nearly flat, stable price movement."),
            ("02","#80a0ff","Frequency","Determines how rapidly price cycles through its wave pattern. High frequency = erratic intraday trading. Low frequency = gradual macro-driven cycles."),
            ("03","#00cc80","Positive Drift","Adds a linear upward component to the price. A positive drift value means the baseline rises consistently over time — simulating a bullish, growing market."),
            ("04","#ff6060","Negative Drift","When drift is negative, the price baseline falls steadily — representing a bearish market, sell-offs, or declining investor interest."),
            ("05","#ffaa40","Noise","Sampled from a normal distribution. Higher noise makes the chart jagged and erratic, simulating real-world market shocks and sentiment shifts."),
        ]

        selected_fc = st.radio("", [x[2] for x in fc_items], horizontal=True, key="fc_select", label_visibility="collapsed")

        for num, color, name, body in fc_items:
            if selected_fc == name:
                card_html = (
                    '<div style="margin:0 32px 16px;background:rgba(4,12,40,0.95);border:1px solid '
                    + color + ';border-top:3px solid ' + color + ';border-radius:12px;padding:20px 24px;'
                    'box-shadow:0 0 24px ' + color + '22;">'
                    '<div style="font-family:Orbitron,monospace;font-size:10px;font-weight:700;color:'
                    + color + ';letter-spacing:2px;margin-bottom:10px;">' + num + ' / 05 &nbsp;·&nbsp; ' + name.upper() + '</div>'
                    '<div style="font-size:13px;color:rgba(200,220,255,0.8);line-height:1.8;">' + body + '</div>'
                    '</div>'
                )
                st.markdown(card_html, unsafe_allow_html=True)
                break

        # ── Section 6: Automated Analysis Report ──────────────────────────────
        trend_word = "Bullish (Upward)" if c_drift > 0 else "Bearish (Downward)" if c_drift < 0 else "Neutral (Sideways)"
        stability  = "Highly Stable" if std_price < 5 else "Moderately Stable" if std_price < 15 else "Highly Unstable"
        freq_desc  = "Rapid oscillations" if c_frequency > 0.5 else "Moderate cycles" if c_frequency > 0.2 else "Slow long-term cycles"
        conclusion = ("This simulation demonstrates that mathematical models can effectively replicate "
            "the core properties of cryptocurrency markets. The sine-based model captures cyclical "
            "patterns, drift represents macro trends, and Gaussian noise models unpredictable market "
            "events. Understanding these components allows analysts to build sophisticated pricing "
            "models, risk frameworks, and trading strategies.")
        drift_color      = "#00cc80" if c_drift > 0 else "#ff6060" if c_drift < 0 else "#80a0ff"
        vol_report_color = "#00cc80" if vol_level == "LOW" else "#ffaa40" if vol_level == "MEDIUM" else "#ff4466"

        st.markdown("""
        <div class="card" style="margin-top:20px;">
            <div class="card-title">&#128196; Section 6 — Automated Analysis Report</div>
        </div>
        """, unsafe_allow_html=True)

        r1, r2, r3, r4 = st.columns(4)
        with r1:
            st.markdown(
                '<div style="background:rgba(0,50,150,0.12);border:1px solid rgba(0,100,200,0.22);border-radius:8px;padding:14px;">'
                '<div style="font-size:9px;color:rgba(160,196,255,0.45);letter-spacing:2px;font-family:monospace;margin-bottom:6px;">VOLATILITY LEVEL</div>'
                '<div style="font-size:15px;font-weight:700;color:' + vol_report_color + ';">' + vol_level + '</div>'
                '<div style="font-size:11px;color:rgba(160,196,255,0.55);margin-top:3px;">'
                + f"σ={std_price:.4f} · Var={var_price:.4f}" + '</div></div>',
                unsafe_allow_html=True)
        with r2:
            st.markdown(
                '<div style="background:rgba(0,50,150,0.12);border:1px solid rgba(0,100,200,0.22);border-radius:8px;padding:14px;">'
                '<div style="font-size:9px;color:rgba(160,196,255,0.45);letter-spacing:2px;font-family:monospace;margin-bottom:6px;">MARKET TREND</div>'
                '<div style="font-size:15px;font-weight:700;color:' + drift_color + ';">' + trend_word + '</div>'
                '<div style="font-size:11px;color:rgba(160,196,255,0.55);margin-top:3px;">'
                + f"Drift={c_drift:+.2f} per period" + '</div></div>',
                unsafe_allow_html=True)
        with r3:
            st.markdown(
                '<div style="background:rgba(0,50,150,0.12);border:1px solid rgba(0,100,200,0.22);border-radius:8px;padding:14px;">'
                '<div style="font-size:9px;color:rgba(160,196,255,0.45);letter-spacing:2px;font-family:monospace;margin-bottom:6px;">STABILITY</div>'
                '<div style="font-size:15px;font-weight:700;color:#a0c8ff;">' + stability + '</div>'
                '<div style="font-size:11px;color:rgba(160,196,255,0.55);margin-top:3px;">'
                + f"Mean=${mean_price:,.2f} · Ret={mean_return:.4f}%" + '</div></div>',
                unsafe_allow_html=True)
        with r4:
            st.markdown(
                '<div style="background:rgba(0,50,150,0.12);border:1px solid rgba(0,100,200,0.22);border-radius:8px;padding:14px;">'
                '<div style="font-size:9px;color:rgba(160,196,255,0.45);letter-spacing:2px;font-family:monospace;margin-bottom:6px;">OSCILLATION</div>'
                '<div style="font-size:15px;font-weight:700;color:#80a0ff;">' + freq_desc + '</div>'
                '<div style="font-size:11px;color:rgba(160,196,255,0.55);margin-top:3px;">'
                + f"F={c_frequency:.2f} · A={c_amplitude}" + '</div></div>',
                unsafe_allow_html=True)

        st.markdown(
            '<div style="margin:16px 32px 0;padding:16px 20px;background:rgba(4,12,35,0.7);border:1px solid rgba(0,100,200,0.2);border-radius:10px;">'
            '<div style="font-size:9px;color:rgba(0,200,255,0.4);letter-spacing:2px;font-family:monospace;margin-bottom:8px;">LEARNING CONCLUSION</div>'
            '<div style="font-size:13px;color:rgba(180,210,255,0.75);line-height:1.85;">' + conclusion + '</div>'
            '<div style="margin-top:12px;font-size:9px;color:rgba(100,140,200,0.35);font-family:monospace;'
            'border-top:1px solid rgba(0,100,200,0.12);padding-top:10px;display:flex;justify-content:space-between;">'
            '<span>GENERATED AUTOMATICALLY</span>'
            + '<span>' + f"N={c_time_steps} A={c_amplitude} F={c_frequency:.2f} D={c_drift:+.2f} noise={c_noise}" + '</span>'
            '</div></div>',
            unsafe_allow_html=True)

    # ── Footer bar ────────────────────────────────────────────────────────────
    st.markdown('<hr>', unsafe_allow_html=True)
    fl, fr = st.columns([5, 1])
    with fl:
        st.markdown("""
        <div style="padding:8px 32px; font-family:'Share Tech Mono',monospace; font-size:11px; color:rgba(100,140,200,0.4);">
            AEROSPACE DATA INSIGHTS PLATFORM &nbsp;&#183;&nbsp; SYS:NOMINAL &nbsp;&#183;&nbsp; DATA_INTEGRITY:VERIFIED
        </div>
        """, unsafe_allow_html=True)
    with fr:
        if st.button("LOGOUT", key="logout_btn"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            if "sim_results" in st.session_state:
                del st.session_state["sim_results"]
            st.rerun()
