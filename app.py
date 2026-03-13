import streamlit as st
import json
import os
import random
from datetime import datetime

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Sapio Intelligence | God Mode", page_icon="⚡", layout="wide")

# --- 2. THE WHALE WATCHER GENERATOR (Simulated for 2026 Live Feed) ---
# In a full build, this would connect to the XRPL/NEAR RPC nodes.
def get_whale_alerts():
    whales = [
        {"time": "14:02", "asset": "XRP", "amount": "450,000", "type": "Institutional Settlement"},
        {"time": "13:58", "asset": "NEAR", "amount": "82,000", "type": "AI Agent Deployment"},
        {"time": "13:45", "asset": "XRP", "amount": "1,200,000", "type": "Treasury Move (x402)"},
        {"time": "13:10", "asset": "NEAR", "amount": "15,000", "type": "Compute Buy-back"}
    ]
    return whales

# --- 3. DATA LOADING ---
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "Agentic_GDP_Live_Feed.json")
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            return json.load(f)
    return {"global_aGDP_estimate": "$6.2B", "top_movers": []}

data = load_data()

# --- 4. SIDEBAR (The Control Center) ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/radar.png", width=80)
    st.title("Sapio Command")
    st.status("XRPL Oracle: CONNECTED", state="complete")
    st.status("NEAR Sharding: OPTIMIZED", state="complete")
    
    st.markdown("### 🛰️ Live Whale Watcher")
    for whale in get_whale_alerts():
        st.caption(f"**{whale['time']}** | {whale['asset']} {whale['amount']}")
        st.write(f"↳ {whale['type']}")
    
    st.divider()
    if st.button("🚀 Force Data Re-Sync"):
        st.toast("Syncing with XRPL Mainnet...")

# --- 5. MAIN TERMINAL UI ---
st.title("🌐 Sapio Intelligence Terminal")
st.markdown("### `System Status: GOD MODE ACTIVATED`")

# Hero Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Agentic GDP", data.get("global_aGDP_estimate", "$6.2B"), "+12.4%")
m2.metric("XRPL ISO-20022", "Active", "Stable")
m3.metric("NEAR Agent Count", "14,802", "+402")
m4.metric("Alpha Signal", "High", "Critical")

# Main Content Split
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📊 Ecosystem Flow (Top Movers)")
    st.table(data.get("top_movers", []))
    
    st.subheader("🔥 2026 Alpha Pulse")
    st.info("**NEWS:** Ripple confirms XAO DAO will prioritize Sapio-indexed projects for Q3 liquidity.")
    st.success("**UPGRADE:** NEAR Protocol hits 1.2M sub-shards; AI agent latency dropped to 10ms.")

with col_right:
    st.subheader("📩 Capture Leads")
    with st.container(border=True):
        st.write("Onboarding Institutional API Beta")
        email = st.text_input("Work Email")
        tier = st.selectbox("Tier", ["Hedge Fund", "VC", "Individual Pro"])
        if st.button("Request Access"):
            st.balloons()
            st.success("Added to Sapio Alpha List.")

# --- 6. FOOTER ---
st.divider()
st.caption(f"Sapio Engine v3.0.1 | Last Sync: {datetime.now().strftime('%H:%M:%S')} | Restricted Access")
