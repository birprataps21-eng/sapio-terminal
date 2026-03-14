import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. SETTINGS & BRAIN ---
st.set_page_config(page_title="Sapio Intelligence | v8.5", page_icon="⚡", layout="wide")

@st.cache_resource
def get_global_treasury():
    return {"revenue": 1240.50, "missions": 412}

treasury = get_global_treasury()

# --- 2. LIVE DATA FETCHING ---
def get_crypto_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin&vs_currencies=usd&include_24hr_change=true"
        return requests.get(url).json()
    except:
        return None

# --- 3. SESSION STATE ---
if 'wallet_address' not in st.session_state:
    st.session_state.wallet_address = None
if 'total_revenue' not in st.session_state:
    st.session_state.total_revenue = treasury["revenue"]

# --- 4. HEADER: LIVE MARKET BAR ---
prices = get_crypto_prices()
if prices:
    p_xrp, c_xrp = prices['ripple']['usd'], prices['ripple']['usd_24h_change']
    p_near, c_near = prices['near']['usd'], prices['near']['usd_24h_change']
    st.markdown(f"""
        <div style="background:#1a1c24; padding:15px; border-radius:10px; border-bottom: 2px solid #00ffcc; margin-bottom: 20px;">
            <span style="color:white; margin-right:20px;"><b>LIVE TERMINAL</b></span>
            <span style="color:#00ffcc;">XRP: ${p_xrp} ({round(c_xrp, 2)}%)</span> | 
            <span style="color:#00ffcc; margin-left:15px;">NEAR: ${p_near} ({round(c_near, 2)}%)</span>
        </div>
    """, unsafe_allow_html=True)

# --- 5. THE GRID LAYOUT (The Secret to Not Losing Data) ---
# We split the screen into 3 main columns
col_sidebar, col_main, col_data = st.columns([1, 2, 1])

# --- COLUMN 1: CONTROLS ---
with col_sidebar:
    st.subheader("👤 Wallet")
    if not st.session_state.wallet_address:
        if st.button("🔗 Connect Wallet", use_container_width=True):
            st.session_state.wallet_address = f"r{random.randint(1000, 9999)}...xP"
            st.rerun()
    else:
        st.success(f"ID: {st.session_state.wallet_address}")
    
    st.divider()
    st.subheader("💰 Treasury")
    st.metric("Total Revenue", f"${round(st.session_state.total_revenue, 2)}")

# --- COLUMN 2: EXECUTION ---
with col_main:
    st.subheader("⚡ Intent Mission Engine")
    with st.container(border=True):
        mission = st.text_input("Define Mission", placeholder="Optimize yields...", disabled=not st.session_state.wallet_address)
        if st.button("🚀 Deploy to Cloud", use_container_width=True, disabled=not st.session_state.wallet_address):
            with st.status("Solving..."):
                time.sleep(1)
                fee = round(random.uniform(0.10, 0.95), 2)
                st.session_state.total_revenue += fee
                treasury["revenue"] = st.session_state.total_revenue
            st.success(f"Success! Collected ${fee}")
    
    st.subheader("💹 Market Sentiment")
    chart_data = pd.DataFrame(random.sample(range(50, 100), 10), columns=['Efficiency'])
    st.line_chart(chart_data, color="#00ffcc")

# --- COLUMN 3: LEADERBOARD ---
with col_data:
    st.subheader("🏆 Top Agents")
    st.table(pd.DataFrame([
        {"Agent": "Alpha-1", "Profit": "$412"},
        {"Agent": "Whale-Bot", "Profit": "$389"},
        {"Agent": "Sapio-Yield", "Profit": "$210"}
    ]))
    
    st.subheader("🛰️ System Logs")
    st.caption("● XRPL Node: Operational")
    st.caption("● NEAR Shard: Latency 14ms")
    st.caption(f"● Last Sync: {datetime.now().strftime('%H:%M:%S')}")
