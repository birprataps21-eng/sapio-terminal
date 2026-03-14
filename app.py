import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. CORE CONFIG & ADVANCED UI ---
st.set_page_config(page_title="Sapio Intelligence | Institutional Terminal", page_icon="⚡", layout="wide")

# High-Density Professional CSS
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    
    /* Institutional Glass Cards */
    div.stElementContainer div[data-testid="stVerticalBlock"] > div {
        background: rgba(13, 17, 23, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Data Highlighting */
    [data-testid="stMetricValue"] { font-size: 1.6rem !important; color: #00ffcc !important; font-family: 'Courier New', monospace; }
    
    /* Global Status Bar */
    .status-bar {
        background: #0d1117;
        border-bottom: 1px solid #00ffcc;
        padding: 5px 20px;
        font-size: 0.8rem;
        color: #8b949e;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00ffcc 0%, #00ccff 100%);
        color: #05070a !important;
        font-weight: 800;
        border: none;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 15px rgba(0, 255, 204, 0.3); }
    </style>
""", unsafe_allow_html=True)

# --- 2. DATA ENGINES ---
@st.cache_resource
def get_global_data():
    return {
        "revenue": 1240.50, 
        "missions": 412,
        "history": [1050, 1100, 1150, 1180, 1240],
        "apy": {"XRPL": 12.4, "NEAR": 8.1, "SOL": 6.4}
    }

def get_market_data():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
        return requests.get(url).json()
    except: return None

store = get_global_data()
prices = get_market_data()

# --- 3. SESSION STATE ---
if 'wallet_address' not in st.session_state: st.session_state.wallet_address = None
if 'total_revenue' not in st.session_state: st.session_state.total_revenue = store["revenue"]

# --- 4. TOP NAV: MULTI-COIN STRIP ---
t_col1, t_col2, t_col3, t_col4, t_col5 = st.columns([2, 1, 1, 1, 1])
with t_col1: st.title("⚡ SAPIO INTEL")
if prices:
    with t_col2: st.metric("XRP", f"${prices['ripple']['usd']}", f"{round(prices['ripple']['usd_24h_change'], 1)}%")
    with t_col3: st.metric("NEAR", f"${prices['near']['usd']}", f"{round(prices['near']['usd_24h_change'], 1)}%")
    with t_col4: st.metric("BTC", f"${prices['bitcoin']['usd']}", f"{round(prices['bitcoin']['usd_24h_change'], 1)}%")
    with t_col5: st.metric("ETH", f"${prices['ethereum']['usd']}", f"{round(prices['ethereum']['usd_24h_change'], 1)}%")

st.divider()

# --- 5. QUAD-ZONE TERMINAL LAYOUT ---
# We use a 4-column layout to fill the screen professionally
col1, col2, col3, col4 = st.columns([1.2, 2.5, 1.5, 1.2])

# -- ZONE 1: TREASURY & AUTH --
with col1:
    st.markdown("### 🏦 Platform Finance")
    st.metric("Total Gross Revenue", f"${round(st.session_state.total_revenue, 2)}", "+$42.50")
    st.metric("Total AI Missions", store["missions"], "+12")
    
    st.divider()
    st.markdown("### 🔐 Authentication")
    if not st.session_state.wallet_address:
        if st.button("CONNECT CORPORATE ID"):
            st.session_state.wallet_address = f"r{random.randint(100, 999)}...SAPIO"
            st.rerun()
    else:
        st.success(f"SECURE: {st.session_state.wallet_address}")
        if st.button("DISCONNECT"):
            st.session_state.wallet_address = None
            st.rerun()

# -- ZONE 2: COMMAND & EXECUTION --
with col2:
    st.markdown("### ⚡ Intent Command Center")
    with st.container():
        mission = st.text_input("Define On-Chain Intent", placeholder="e.g. Execute arbitrage on XRPL DEX...", disabled=not st.session_state.wallet_address)
        if st.button("DEPLOY TO SAPIO GLOBAL CLOUD", disabled=not st.session_state.wallet_address):
            with st.status("Solving via Sapio Agentic Network..."):
                time.sleep(1.2)
                fee = round(random.uniform(0.15, 0.85), 2)
                st.session_state.total_revenue += fee
                store["revenue"] = st.session_state.total_revenue
                store["missions"] += 1
                store["history"].append(st.session_state.total_revenue)
            st.success(f"Mission Signed. Platform Fee: ${fee}")
            st.balloons()
    
    st.markdown("### 💹 Institutional Revenue Growth")
    st.area_chart(store["history"], color="#00ffcc")

# -- ZONE 3: APY & AGENTS --
with col3:
    st.markdown("### 💎 Live Alpha Yields (APY)")
    st.write(f"● **XRPL Yield Pool:** {store['apy']['XRPL']}%")
    st.progress(store['apy']['XRPL'] / 20)
    st.write(f"● **NEAR Staking Hub:** {store['apy']['NEAR']}%")
    st.progress(store['apy']['NEAR'] / 20)
    
    st.divider()
    st.markdown("### 🏆 Active Agents")
    st.dataframe(pd.DataFrame([
        {"Agent": "Alpha-1", "Profit": "$412"},
        {"Agent": "Whale", "Profit": "$389"},
        {"Agent": "Yield", "Profit": "$210"}
    ]), hide_index=True, use_container_width=True)

# -- ZONE 4: GLOBAL INFRASTRUCTURE --
with col4:
    st.markdown("### 🛰️ System Health")
    st.caption("🟢 LONDON (LN-1): ACTIVE")
    st.caption("🟢 SINGAPORE (SG-4): ACTIVE")
    st.caption("🟡 NEW YORK (NY-2): SYNCING")
    
    st.divider()
    st.markdown("### 🕵️ Whale Alert")
    st.code("4.2M XRP → UNKNOWN WALLET\n142k NEAR → LIQUIDITY POOL", language="text")
    
    st.divider()
    st.markdown("### 📊 Valuation Forecast")
    st.metric("Projected Val.", "$14.8M", "+12%")

# --- 6. FOOTER ---
st.markdown("---")
st.caption(f"SAPIO INTEL CORP | PROPRIETARY TRADING TERMINAL v10.0 | SYSTEM TIME: {datetime.now().strftime('%H:%M:%S')}")
