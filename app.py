import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. INSTITUTIONAL THEMING (The Professional Secret) ---
st.set_page_config(page_title="Sapio Intelligence Terminal", page_icon="⚡", layout="wide")

# Custom CSS for the "Team-Built" look
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #05070a;
        color: #e0e0e0;
    }
    
    /* Custom Card Styling */
    div.stElementContainer div[data-testid="stVerticalBlock"] > div {
        background-color: #0d1117;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s ease;
    }
    
    div.stElementContainer div[data-testid="stVerticalBlock"] > div:hover {
        border-color: #00ffcc;
        box-shadow: 0px 0px 15px rgba(0, 255, 204, 0.1);
    }

    /* Professional Metric Styling */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #00ffcc !important;
    }

    /* Glowing Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0a0d12 !important;
        border-right: 1px solid #1f2937;
    }

    /* Buttons that look like FinTech */
    .stButton>button {
        background: linear-gradient(90deg, #00ffcc 0%, #00ccff 100%);
        color: #05070a !important;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. DATA ENGINES ---
@st.cache_resource
def get_global_treasury():
    return {"revenue": 1240.50, "missions": 412}

def get_live_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin&vs_currencies=usd&include_24hr_change=true"
        return requests.get(url).json()
    except: return None

treasury = get_global_treasury()

# --- 3. LOGIC & STATE ---
if 'wallet_address' not in st.session_state:
    st.session_state.wallet_address = None
if 'total_revenue' not in st.session_state:
    st.session_state.total_revenue = treasury["revenue"]

# --- 4. NAVIGATION / TOP BAR ---
prices = get_live_prices()
t1, t2, t3, t4 = st.columns([2, 1, 1, 1])
with t1:
    st.title("⚡ SAPIO INTEL")
with t2:
    if prices:
        st.metric("XRP/USD", f"${prices['ripple']['usd']}", f"{round(prices['ripple']['usd_24h_change'], 2)}%")
with t3:
    if prices:
        st.metric("NEAR/USD", f"${prices['near']['usd']}", f"{round(prices['near']['usd_24h_change'], 2)}%")
with t4:
    st.metric("NETWORK STATUS", "OPTIMAL", delta="14ms")

st.divider()

# --- 5. MAIN TERMINAL LAYOUT ---
col_sidebar, col_main = st.columns([1, 3])

with col_sidebar:
    st.markdown("### 🔐 Security Hub")
    if not st.session_state.wallet_address:
        if st.button("CONNECT CORPORATE WALLET"):
            st.session_state.wallet_address = f"r{random.randint(100, 999)}...Sapio"
            st.rerun()
    else:
        st.success(f"ID: {st.session_state.wallet_address}")
    
    st.divider()
    st.markdown("### 🏦 Platform Treasury")
    st.metric("Gross Revenue (USDC)", f"${round(st.session_state.total_revenue, 2)}")
    
    st.divider()
    st.markdown("### 🛰️ Live Logs")
    st.caption("● Node-Alpha-4: Active")
    st.caption("● Intent-Relay: Verified")

with col_main:
    # Mission Center
    m_col1, m_col2 = st.columns([2, 1])
    with m_col1:
        st.markdown("### ⚡ Deploy Autonomous Intent")
        with st.container():
            mission = st.text_input("Enter Institutional Mission", placeholder="e.g. Sweep XRPL liquidity if pool > 1M", disabled=not st.session_state.wallet_address)
            if st.button("DEPLOY TO SAPIO CLOUD", disabled=not st.session_state.wallet_address):
                with st.status("Solving via Sapio Agentic Network..."):
                    time.sleep(1.5)
                    fee = round(random.uniform(0.10, 0.95), 2)
                    st.session_state.total_revenue += fee
                    treasury["revenue"] = st.session_state.total_revenue
                st.success(f"Mission Executed. Platform Fee: ${fee}")
                st.balloons()
    
    with m_col2:
        st.markdown("### 🏆 Performance")
        st.dataframe(pd.DataFrame([
            {"Agent": "Alpha-1", "Profit": "$412"},
            {"Agent": "Whale", "Profit": "$389"},
            {"Agent": "Yield", "Profit": "$210"}
        ]), hide_index=True)

    # Market Intelligence Chart
    st.markdown("### 💹 Market Sentiment Analysis")
    chart_data = pd.DataFrame(random.sample(range(60, 100), 20), columns=['AI Confidence'])
    st.area_chart(chart_data, color="#00ffcc")

st.markdown("---")
st.caption(f"Proprietary Technology of Sapio Intel Corp © 2026 | Deployment Version 9.0.4")
