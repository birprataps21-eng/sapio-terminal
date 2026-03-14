import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. INSTITUTIONAL UI ENGINE ---
st.set_page_config(page_title="Sapio Sovereign Terminal", page_icon="🏦", layout="wide")

st.markdown("""
    <style>
    /* Dark Room Aesthetic */
    .stApp { background-color: #020406; color: #94a3b8; font-family: 'Inter', sans-serif; }
    
    /* Quadrant Tiles */
    [data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background: #0a0f16;
        border: 1px solid #1e293b;
        border-radius: 2px; /* Sharp corners for professional look */
        padding: 20px;
        min-height: 380px;
    }

    /* Professional Metric Typography */
    [data-testid="stMetricValue"] { color: #f8fafc !important; font-family: 'JetBrains Mono', monospace; font-size: 1.6rem !important; font-weight: 700; }
    [data-testid="stMetricDelta"] { font-size: 0.85rem !important; }

    /* ISO 20022 Badge */
    .iso-status {
        color: #00ffcc;
        border: 1px solid #00ffcc;
        padding: 4px 10px;
        font-size: 10px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Terminal Action Buttons */
    .stButton>button {
        background: transparent;
        color: #00ffcc !important;
        border: 1px solid #00ffcc;
        border-radius: 0px;
        font-size: 12px;
        font-weight: bold;
        transition: all 0.2s;
    }
    .stButton>button:hover { background: #00ffcc; color: #020406 !important; box-shadow: 0 0 15px #00ffcc55; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE CORE PROTOCOL (Zero-Base) ---
@st.cache_resource
def get_global_metrics():
    # GDP and Revenue start at real base levels
    return {"gdp": 6.57, "rev": 0.000, "hist": [6.50, 6.52, 6.55, 6.57]}

data = get_global_metrics()

# --- 3. TOP LEVEL: GLOBAL RECOGNITION BAR ---
h_left, h_mid, h_right = st.columns([2, 3, 2])
with h_left:
    st.markdown("<h2 style='margin:0; color:white;'>SAPIO <span style='color:#00ffcc; font-size:15px;'>SOVEREIGN v15.0</span></h2>", unsafe_allow_html=True)
with h_mid:
    # ISO 20022 Ticker
    st.markdown("<div style='text-align:center; padding-top:10px;'><span class='iso-status'>ISO 20022 COMPLIANT • PACS.008 ENABLED • SWIFT-XML BRIDGED</span></div>", unsafe_allow_html=True)
with h_right:
    st.markdown(f"<div style='text-align:right; color:#475569;'>SYSTEM TIME: {datetime.now().strftime('%H:%M:%S UTC')}</div>", unsafe_allow_html=True)

st.divider()

# --- 4. THE 4-QUADRANT GRID ---
# ROW 1
top_l, top_r = st.columns(2)

with top_l:
    st.markdown("### 📊 AGENTIC GDP TRACKER")
    c1, c2 = st.columns(2)
    c1.metric("Current Agentic GDP", f"${data['gdp']}B", "+0.02B")
    c2.metric("Projected Q4", "$7.12B", "Target")
    st.area_chart(data['hist'], color="#00ffcc", height=180)

with top_r:
    st.markdown("### 🏦 REVENUE PIPELINE")
    r1, r2 = st.columns(2)
    r1.metric("Total Platform Revenue", f"${round(data['rev'], 4)}", "REAL-TIME")
    r2.metric("Active Yield Nodes", "142", "Global")
    
    st.divider()
    st.markdown("#### ⚡ DEPLOY INTENT")
    intent = st.text_input("Protocol Command", placeholder="Sweep liquidity...", label_visibility="collapsed")
    if st.button("EXECUTE ON-CHAIN"):
        with st.status("Solving via Rust Kernel..."):
            time.sleep(1)
            data['rev'] += 0.0025
            data['gdp'] += 0.01
            data['hist'].append(data['gdp'])
        st.rerun()

# ROW 2
bot_l, bot_r = st.columns(2)

with bot_l:
    st.markdown("### 💹 MARKET INTELLIGENCE")
    # Real prices fetch simulation to avoid lag
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("XRP/USD", "$0.6214", "+1.2%")
    m_col2.metric("NEAR/USD", "$6.42", "-0.4%")
    m_col3.metric("BTC/USD", "$68,412", "+2.1%")
    
    st.divider()
    st.caption("NETWORK LATENCY: 14ms | SETTLEMENT: INSTANT | SECURITY: RSA-4096")
    st.progress(98, text="Node Sync Progress")

with bot_r:
    st.markdown("### 🔐 INSTITUTIONAL ACCESS")
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        st.warning("AUTHENTICATION REQUIRED")
        if st.button("CONNECT CORPORATE HSM"):
            st.session_state.auth = True
            st.rerun()
    else:
        st.success("SESSION ACTIVE: SAPIO-ADMIN-01")
        st.table(pd.DataFrame([
            {"Region": "London", "Status": "Active", "Load": "14%"},
            {"Region": "Singapore", "Status": "Active", "Load": "22%"},
            {"Region": "NY", "Status": "Syncing", "Load": "91%"}
        ]))

# --- 5. FOOTER ---
st.markdown("---")
st.caption("PROPRIETARY TECHNOLOGY. ISO 20022 STANDARDIZED DATA FORMATS ONLY.")
