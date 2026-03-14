import streamlit as st
import pandas as pd
import random
import time
import requests # NEW: For pulling live data from the web
from datetime import datetime

# --- 1. LIVE DATA ENGINE (The Real Stuff) ---
def get_crypto_prices():
    try:
        # Fetching real prices for XRP and NEAR
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url).json()
        return response
    except:
        # Fallback if the API is busy
        return None

# --- 2. THE BRAIN (Treasury) ---
@st.cache_resource
def get_global_treasury():
    return {"revenue": 1240.50, "missions": 412}

treasury = get_global_treasury()

# --- 3. PAGE CONFIG ---
st.set_page_config(page_title="Sapio Intelligence | v8.0", page_icon="⚡", layout="wide")

# --- 4. SESSION STATE ---
if 'wallet_address' not in st.session_state:
    st.session_state.wallet_address = None
if 'total_revenue' not in st.session_state:
    st.session_state.total_revenue = treasury["revenue"]

# --- 5. LIVE MARKET HEADER ---
prices = get_crypto_prices()
if prices:
    p_xrp = prices['ripple']['usd']
    c_xrp = prices['ripple']['usd_24h_change']
    p_near = prices['near']['usd']
    c_near = prices['near']['usd_24h_change']
    
    st.markdown(f"""
        <div style="display: flex; gap: 20px; background: #1a1c24; padding: 10px; border-radius: 5px; border-left: 5px solid #00ffcc;">
            <span style="color: white;"><b>LIVE MARKET:</b></span>
            <span style="color: #00ffcc;">XRP: ${p_xrp} ({round(c_xrp, 2)}%)</span>
            <span style="color: #00ffcc;">NEAR: ${p_near} ({round(c_near, 2)}%)</span>
        </div>
    """, unsafe_allow_html=True)

# --- 6. SIDEBAR & WALLET ---
with st.sidebar:
    st.title("Sapio Command")
    if not st.session_state.wallet_address:
        if st.button("🔗 Connect Wallet", use_container_width=True):
            st.session_state.wallet_address = f"r{random.randint(1000, 9999)}...xP"
            st.rerun()
    else:
        st.success(f"Connected: {st.session_state.wallet_address}")
    
    st.divider()
    st.metric("Total Platform Revenue", f"${round(st.session_state.total_revenue, 2)}")

# --- 7. MAIN DASHBOARD ---
st.title("🌐 Sapio Intelligence Terminal")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("🤖 Agent Status")
    st.write("● Alpha-1: **Scanning Nodes**")
    st.write("● Whale-Bot: **Monitoring Pools**")

with col2:
    st.subheader("⚡ Intent Solver")
    mission = st.text_input("Define Mission", placeholder="Harvest yield...", disabled=not st.session_state.wallet_address)
    if st.button("🚀 Execute", disabled=not st.session_state.wallet_address):
        with st.status("Solving..."):
            time.sleep(1)
            fee = round(random.uniform(0.10, 0.95), 2)
            st.session_state.total_revenue += fee
            treasury["revenue"] = st.session_state.total_revenue
        st.success(f"Mission Success! Fee: ${fee}")

with col3:
    st.subheader("📊 Network Health")
    st.progress(98, text="XRPL Node Sync")
    st.progress(85, text="NEAR Shard Load")

# --- 8. REAL-TIME CHART ---
st.divider()
st.subheader("💹 Market Intelligence")
# This creates a dummy chart that looks real for the dashboard
chart_data = pd.DataFrame(random.sample(range(60, 100), 10), columns=['Price'])
st.area_chart(chart_data, color="#00ffcc")

st.caption(f"v8.0 Advanced Terminal | Last Sync: {datetime.now().strftime('%H:%M:%S')}")
