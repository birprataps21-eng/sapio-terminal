import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# --- 1. THE BRAIN (Persistent Data without a Database) ---
# We use st.cache_resource to keep the revenue alive even if the page refreshes.
@st.cache_resource
def get_global_treasury():
    return {"revenue": 1240.50, "missions": 412} # Starting 'Seed' data

treasury = get_global_treasury()

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Sapio Intelligence | Global", page_icon="⚡", layout="wide")

# --- 3. SESSION STATE ---
if 'total_revenue' not in st.session_state:
    st.session_state.total_revenue = treasury["revenue"]
if 'missions_completed' not in st.session_state:
    st.session_state.missions_completed = treasury["missions"]

# --- 4. DATA FEED ---
def get_live_data():
    return {
        "gdp_val": f"${round(random.uniform(6.5, 6.8), 2)}B",
        "movers": [
            {"Project": "LiquidX (XRPL)", "Volume": "$142M", "Trend": "🚀 High"},
            {"Project": "NearScribe AI", "Volume": "$54M", "Trend": "📈 Steady"},
            {"Project": "Sapio Oracle", "Volume": "$18M", "Trend": "🔥 New"}
        ],
        "news": ["SYSTEM: Cloud Sync Active", "XRPL: x402 Node Online", "NEAR: AI Compute Demand Spike"]
    }

data = get_live_data()

# --- 5. SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/radar.png", width=60)
    st.title("Sapio Command")
    st.success("✓ CLOUD STATUS: LIVE")
    st.divider()
    st.markdown("### 🏦 Global Treasury")
    st.metric("Total Revenue", f"${round(st.session_state.total_revenue, 2)}", f"+{st.session_state.missions_completed} missions")
    st.divider()
    st.info("Agentic GDP is scaling. Missions authorized for XRPL/NEAR.")

# --- 6. MAIN UI ---
st.title("🌐 Sapio Intelligence Terminal")
st.markdown("### `Production Tier: GLOBAL HOSTING READY`")

# TICKER
news_string = " • ".join(data["news"])
st.markdown(f"""
    <div style="background-color: #0e1117; padding: 12px; border-radius: 10px; border: 2px solid #00ffcc;">
        <marquee style="color: #00ffcc; font-family: 'Courier New'; font-weight: bold;">
            [LIVE ALPHA FEED] • {news_string} • Platform Revenue: ${round(st.session_state.total_revenue, 2)}
        </marquee>
    </div>
""", unsafe_allow_html=True)

# METRICS
st.write("")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Agentic GDP", data["gdp_val"], "+14.2%")
m2.metric("Missions Run", st.session_state.missions_completed, "Global")
m3.metric("Platform Fee", "0.15%", "Fixed")
m4.metric("AI Confidence", "98.4%", "Optimal")

# --- 7. COMMAND CENTER ---
st.divider()
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("⚡ Deploy Autonomous Intent")
    with st.container(border=True):
        mission = st.text_input("Define Mission", placeholder="e.g. 'Optimize XRPL liquidity for 12% APY'")
        if st.button("🚀 Execute on Cloud"):
            with st.status("Deploying to Sapio Cloud Nodes..."):
                time.sleep(1.5)
                fee = round(random.uniform(0.10, 0.95), 2)
                st.session_state.total_revenue += fee
                st.session_state.missions_completed += 1
                # Update the 'Global' cache
                treasury["revenue"] = st.session_state.total_revenue
                treasury["missions"] = st.session_state.missions_completed
            st.success(f"Mission Signed. Fee Collected: ${fee}")
            st.balloons()

with col_right:
    st.subheader("🏆 Leaderboard")
    st.table(pd.DataFrame([
        {"Agent": "Alpha-1", "Profit": "$412.50"},
        {"Agent": "Whale-Bot", "Profit": "$389.20"},
        {"Agent": "Sapio-Yield", "Profit": "$210.10"}
    ]))

# --- 8. MOVERS ---
st.divider()
st.subheader("🚀 Top Moving Projects")
st.dataframe(pd.DataFrame(data["movers"]), hide_index=True, use_container_width=True)
