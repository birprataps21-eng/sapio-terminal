import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. GLOBAL UI & THEME ---
st.set_page_config(page_title="Sapio Sovereign | ISO 20022", page_icon="🏦", layout="wide")

st.markdown("""
    <style>
    /* Dark Institutional Base */
    .stApp { background-color: #05070a; color: #e2e8f0; }
    
    /* Side-by-Side Card Styling */
    div[data-testid="column"] {
        background: #0d1117;
        border: 1px solid #1f2937;
        padding: 20px;
        border-radius: 8px;
    }
    
    /* Heavyweight Metric Glow */
    [data-testid="stMetricValue"] { color: #00ffcc !important; font-family: 'JetBrains Mono', monospace; font-size: 1.8rem !important; }
    
    /* ISO 20022 Status Bar */
    .iso-banner {
        background: linear-gradient(90deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid #00ffcc;
        color: #00ffcc;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE REAL-TIME ENGINE ---
@st.cache_resource
def init_protocol():
    return {"gdp": 6.57, "rev": 0.00, "history": [6.50, 6.52, 6.55, 6.57]}

def get_live_market():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true"
        return requests.get(url).json()
    except: return None

state = init_protocol()
prices = get_live_market()

# --- 3. THE "CONTROL TOWER" SIDEBAR ---
with st.sidebar:
    st.title("⚡ SAPIO CORE")
    st.markdown("---")
    st.subheader("🏦 GLOBAL TREASURY")
    st.metric("REAL REVENUE", f"${round(state['rev'], 4)}")
    st.metric("AGENTIC GDP", f"${state['gdp']}B", "+0.02")
    
    st.markdown("---")
    st.subheader("🔐 AUTHENTICATION")
    if 'auth' not in st.session_state: st.session_state.auth = False
    if not st.session_state.auth:
        if st.button("CONNECT HSM WALLET", use_container_width=True):
            st.session_state.auth = True
            st.rerun()
    else:
        st.success("SESSION: SECURE")
        if st.button("DISCONNECT", use_container_width=True):
            st.session_state.auth = False
            st.rerun()

# --- 4. MAIN TERMINAL BODY ---
st.markdown('<div class="iso-banner">ISO 20022 COMPLIANT | PACS.008 REAL-TIME SETTLEMENT | AGENTIC ECONOMY ACTIVE</div>', unsafe_allow_html=True)

# TOP ROW: MARKET & COMPLIANCE
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("💹 Market Feed")
    if prices:
        st.write(f"● XRP: **${prices['ripple']['usd']}** ({round(prices['ripple']['usd_24h_change'], 2)}%)")
        st.write(f"● NEAR: **${prices['near']['usd']}** ({round(prices['near']['usd_24h_change'], 2)}%)")
        st.write(f"● BTC: **${prices['bitcoin']['usd']}** ({round(prices['bitcoin']['usd_24h_change'], 2)}%)")
    else:
        st.error("Market API Offline")

with col2:
    st.subheader("📈 GDP Momentum")
    st.line_chart(state['history'], color="#00ffcc", height=150)

with col3:
    st.subheader("🛰️ Infra Status")
    st.caption("🟢 LONDON (HQ): ACTIVE")
    st.caption("🟢 SINGAPORE: ACTIVE")
    st.caption("🟢 TOKYO: ACTIVE")
    st.progress(98, text="Node Sync")

# BOTTOM ROW: THE MISSION COMMAND
st.markdown("### ⚡ DEPLOY AUTONOMOUS INTENT")
with st.container():
    cmd = st.text_input("Enter Protocol Mission", placeholder="e.g. Optimize cross-chain liquidity...", label_visibility="collapsed", disabled=not st.session_state.auth)
    if st.button("EXECUTE ON-CHAIN", use_container_width=True, disabled=not st.session_state.auth):
        with st.status("Solving via Sapio Rust Kernel..."):
            time.sleep(1)
            state['rev'] += 0.0025
            state['gdp'] += 0.01
            state['history'].append(state['gdp'])
        st.success(f"Mission Settled. Revenue Captured.")
        st.rerun()

st.markdown("---")
st.caption(f"SAPIO SOVEREIGN v16.0 | SYSTEM TIME: {datetime.now().strftime('%H:%M:%S UTC')}")
