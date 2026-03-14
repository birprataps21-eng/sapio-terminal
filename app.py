import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. GLOBAL UI CONFIGURATION ---
st.set_page_config(page_title="Sapio Intelligence Terminal", page_icon="⚡", layout="wide")

# Institutional Glassmorphism CSS
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e0e0e0; }
    
    /* Glassmorphism Cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background: rgba(17, 25, 40, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
    }
    
    /* Top Navigation Bar Styling */
    .nav-bar {
        background: rgba(10, 15, 25, 0.9);
        border-bottom: 1px solid #1f2937;
        padding: 1rem;
        border-radius: 0 0 15px 15px;
    }

    /* Metric Customization */
    [data-testid="stMetricValue"] { font-size: 1.8rem !important; color: #00ffcc !important; }
    [data-testid="stMetricDelta"] { font-size: 0.9rem !important; }

    /* Corporate Button Styling */
    .stButton>button {
        background: #00ffcc;
        color: #05070a !important;
        border-radius: 6px;
        font-weight: 600;
        letter-spacing: 0.5px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background: #00ccff; box-shadow: 0 0 20px rgba(0, 255, 204, 0.4); }
    </style>
""", unsafe_allow_html=True)

# --- 2. CORE DATA ENGINES ---
@st.cache_resource
def get_global_treasury():
    return {"revenue": 1240.50, "missions": 412, "history": [1050, 1100, 1150, 1180, 1240]}

def get_market_data():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin&vs_currencies=usd&include_24hr_change=true"
        return requests.get(url).json()
    except: return None

treasury = get_global_treasury()

# --- 3. SESSION & NAVIGATION ---
if 'view_mode' not in st.session_state: st.session_state.view_mode = "Operator"
if 'wallet_address' not in st.session_state: st.session_state.wallet_address = None

# --- 4. TOP NAV BAR ---
prices = get_market_data()
with st.container():
    c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
    with c1: st.title("⚡ SAPIO INTEL")
    with c2: 
        if prices: st.metric("XRP", f"${prices['ripple']['usd']}", f"{round(prices['ripple']['usd_24h_change'], 2)}%")
    with c3:
        if prices: st.metric("NEAR", f"${prices['near']['usd']}", f"{round(prices['near']['usd_24h_change'], 2)}%")
    with c4:
        st.session_state.view_mode = st.radio("Display Mode", ["Operator", "Investor"], horizontal=True, label_visibility="collapsed")

st.divider()

# --- 5. DYNAMIC VIEW LOGIC ---
if st.session_state.view_mode == "Operator":
    # OPERATOR VIEW: Interaction-heavy
    col_ctrl, col_main = st.columns([1, 2.5])
    
    with col_ctrl:
        st.markdown("### 🏦 Platform Treasury")
        st.metric("Gross Revenue", f"${round(treasury['revenue'], 2)}", "Active")
        
        st.divider()
        st.markdown("### 🔑 Authentication")
        if not st.session_state.wallet_address:
            if st.button("CONNECT CORPORATE WALLET", use_container_width=True):
                st.session_state.wallet_address = f"r{random.randint(100, 999)}...SAPIO"
                st.rerun()
        else:
            st.success(f"SECURE: {st.session_state.wallet_address}")
            
    with col_main:
        st.markdown("### ⚡ Intent Mission Center")
        with st.container():
            mission = st.text_input("Define On-Chain Intent", placeholder="e.g. Execute arbitrage on XRPL DEX...", disabled=not st.session_state.wallet_address)
            if st.button("EXECUTE MISSION", disabled=not st.session_state.wallet_address):
                with st.status("Solving Intent..."):
                    time.sleep(1.2)
                    fee = round(random.uniform(0.15, 0.85), 2)
                    treasury["revenue"] += fee
                    treasury["history"].append(treasury["revenue"])
                st.success(f"Success. Fee: ${fee}")

else:
    # INVESTOR VIEW: Growth & Data-heavy
    st.markdown("## 📊 Institutional Performance Report")
    
    inv_col1, inv_col2, inv_col3 = st.columns(3)
    inv_col1.metric("Current Valuation", "$12.4M", "Series A Target")
    inv_col2.metric("Agent Utilization", "94.2%", "+2.1%")
    inv_col3.metric("Platform Fees (Avg)", "$0.52", "Stable")
    
    st.markdown("### 📈 Revenue Growth Curve")
    st.area_chart(treasury["history"], color="#00ffcc")
    
    st.markdown("### 🏆 Top Yield Agents")
    st.table(pd.DataFrame([
        {"Agent": "Alpha-1", "AUM Managed": "$1.2M", "Revenue Gen": "$412"},
        {"Agent": "Whale-Track", "AUM Managed": "$4.5M", "Revenue Gen": "$389"},
        {"Agent": "Yield-Optim", "AUM Managed": "$0.8M", "Revenue Gen": "$210"}
    ]))

# --- 6. FOOTER ---
st.markdown("---")
st.caption(f"Proprietary AI Terminal • v9.5.0 • Last Heartbeat: {datetime.now().strftime('%H:%M:%S')}")
