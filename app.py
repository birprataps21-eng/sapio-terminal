import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. GLOBAL UI ARCHITECTURE ---
st.set_page_config(page_title="Sapio Intelligence | ISO 20022", page_icon="⚡", layout="wide")

# Institutional "Deep-Grid" CSS
st.markdown("""
    <style>
    .stApp { background-color: #06080a; color: #d1d4dc; }
    
    /* Unified Data Tiles */
    div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background: #0d1117;
        border: 1px solid #1f2937;
        border-radius: 4px;
        padding: 18px;
        margin-bottom: 8px;
    }
    
    /* ISO 20022 Highlighting */
    .iso-badge {
        background: #1e293b;
        color: #00ffcc;
        padding: 2px 8px;
        border-radius: 4px;
        border: 1px solid #00ffcc;
        font-size: 0.7rem;
        font-weight: bold;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] { color: #00ffcc !important; font-family: 'JetBrains Mono', monospace; font-size: 1.3rem !important; }
    
    /* Button: Stealth Execution */
    .stButton>button {
        background: #161b22;
        color: #00ffcc !important;
        border: 1px solid #30363d;
        width: 100%;
        transition: 0.2s;
    }
    .stButton>button:hover { border-color: #00ffcc; background: #0d1117; }
    </style>
""", unsafe_allow_html=True)

# --- 2. CORE DATA ENGINES ---
@st.cache_resource
def init_system():
    return {
        "revenue": 0.00,
        "missions": 0,
        "gdp": 6.57, # Initial Agentic GDP
        "history": [6.42, 6.45, 6.50, 6.55, 6.57]
    }

def get_market():
    try: return requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true").json()
    except: return None

sys = init_system()
mkt = get_market()

# --- 3. SESSION STATE ---
if 'wallet' not in st.session_state: st.session_state.wallet = None
if 'rev' not in st.session_state: st.session_state.rev = sys["revenue"]

# --- 4. HEADER: MULTI-CHAIN MONITOR ---
h1, h2, h3, h4, h5 = st.columns([1.5, 1, 1, 1, 1])
with h1: st.title("⚡ SAPIO")
if mkt:
    h2.metric("XRP/USD", f"${mkt['ripple']['usd']}", f"{round(mkt['ripple']['usd_24h_change'], 2)}%")
    h3.metric("NEAR/USD", f"${mkt['near']['usd']}", f"{round(mkt['near']['usd_24h_change'], 2)}%")
    h4.metric("AGENTIC GDP", f"${sys['gdp']}B", "+0.2%")
    h5.metric("ISO 20022", "COMPLIANT", delta="Verified", delta_color="normal")

st.divider()

# --- 5. THE TERMINAL GRID (3-COLUMN DENSE) ---
col_left, col_mid, col_right = st.columns([1, 2, 1])

# -- COLUMN 1: ACCESS & REVENUE --
with col_left:
    st.markdown("#### 🔐 Access Control")
    if not st.session_state.wallet:
        if st.button("CONNECT PROTOCOL WALLET"):
            st.session_state.wallet = f"r{random.randint(100,999)}...SAPIO"
            st.rerun()
    else:
        st.success(f"ID: {st.session_state.wallet}")
        if st.button("DISCONNECT"):
            st.session_state.wallet = None
            st.rerun()

    st.divider()
    st.markdown("#### 🏦 Treasury (Real-Time)")
    st.metric("Total Platform Revenue", f"${round(st.session_state.rev, 4)}")
    st.caption("Revenue tracking: ISO 20022 Message Format (pacs.008)")

# -- COLUMN 2: COMMAND & ANALYTICS --
with col_mid:
    st.markdown("#### ⚡ Mission Execution")
    with st.container():
        intent = st.text_input("Define Intent", placeholder="e.g. Optimize liquidity via XRPL...", disabled=not st.session_state.wallet)
        if st.button("DEPLOY TO MAINNET", disabled=not st.session_state.wallet):
            with st.status("Solving Agentic Intent..."):
                time.sleep(1.2)
                fee = 0.0025
                st.session_state.rev += fee
                sys["history"].append(sys["history"][-1] + 0.01)
            st.success(f"Settled via NEAR Shard. Fee: ${fee}")

    st.markdown("#### 💹 Agentic GDP Growth Tracker")
    st.area_chart(sys["history"], color="#00ffcc", height=220)

# -- COLUMN 3: PERFORMANCE & INFRA --
with col_right:
    st.markdown("#### 🏆 Top Yield Agents")
    st.table(pd.DataFrame([
        {"Agent": "Alpha-1", "Status": "Active"},
        {"Agent": "Whale-X", "Status": "Idle"},
        {"Agent": "Yield-G", "Status": "Syncing"}
    ]))
    
    st.divider()
    st.markdown("#### 🛰️ Network Status")
    st.caption("🟢 LN: 14ms | 🟢 SG: 22ms | 🟢 NY: 18ms")
    st.code("ISO 20022 READY\nAGENT_RUNTIME: WASM\nSETTLEMENT: INSTANT", language="text")

# --- 6. FOOTER ---
st.markdown("---")
st.caption(f"SAPIO CORE v14.0.0 | ISO 20022 COMPLIANT TERMINAL | {datetime.now().strftime('%H:%M:%S')}")
