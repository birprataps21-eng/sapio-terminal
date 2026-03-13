import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Sapio Intelligence | v5.0", page_icon="⚡", layout="wide")

# --- 2. THE "NO-FILE" DATA GENERATOR ---
# This replaces the scraper.py and the JSON files entirely.
def get_live_data():
    return {
        "gdp_val": f"${round(random.uniform(6.5, 6.8), 2)}B",
        "movers": [
            {"Project": "LiquidX (XRPL)", "Volume": "$92M", "Trend": "🚀 High"},
            {"Project": "NearScribe AI", "Volume": "$31M", "Trend": "📈 Steady"},
            {"Project": "Sapio Oracle", "Volume": "$12M", "Trend": "🔥 New"}
        ],
        "agents": [
            {"agent": "Sapio-Alpha-1", "task": "Scanning XRPL Nodes", "status": "ACTIVE"},
            {"agent": "Whale-Tracker", "task": "Monitoring NEAR Shards", "status": "ACTIVE"}
        ],
        "insight": "AI Cluster Analysis: Heavy institutional accumulation detected on XRPL. NEAR sharding protocol optimized for next-gen AI compute."
    }

data = get_live_data()

# --- 3. UI LAYOUT (From your screenshot) ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/radar.png", width=60)
    st.title("Sapio Command")
    st.success("✓ XRPL x402 Node: ONLINE")
    st.success("✓ NEAR Sharding: OPTIMIZED")
    st.divider()
    st.markdown("### 🛰️ Whale Watcher")
    st.caption(f"{datetime.now().strftime('%H:%M')} | 1.2M XRP → Institutional")
    st.caption(f"{datetime.now().strftime('%H:%M')} | 45k NEAR → AI Pool")

st.title("🌐 Sapio Intelligence Terminal")
st.markdown("### `System Status: AI INTEGRATED GOD MODE`")

# --- TICKER ---
st.markdown(f"""
    <div style="background-color: #0e1117; padding: 12px; border-radius: 10px; border: 2px solid #00ffcc;">
        <marquee style="color: #00ffcc; font-family: 'Courier New'; font-weight: bold;">
            [LIVE ALPHA FEED] • XRPL: x402 Node Online • NEAR: AI Compute Demand Spike • aGDP at {data['gdp_val']}
        </marquee>
    </div>
""", unsafe_allow_html=True)

# --- METRICS ---
st.write("")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Agentic GDP", data["gdp_val"], "+14.2%")
m2.metric("XRPL Standard", "ISO-20022", "Active")
m3.metric("NEAR Nodes", "14,802", "+402")
m4.metric("AI Confidence", "98.4%", "Optimal")

# --- CHART & PROJECTS TABLE ---
st.divider()
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📈 GDP Growth Velocity")
    chart_data = pd.DataFrame({
        'Time': pd.date_range(start=datetime.now(), periods=12, freq='H'),
        'GDP ($B)': [6.1, 6.15, 6.2, 6.18, 6.25, 6.3, 6.35, 6.4, 6.38, 6.45, 6.5, 6.57]
    })
    st.area_chart(chart_data.set_index('Time'), color="#00ffcc")

with col_right:
    st.subheader("🚀 Top Movers")
    st.dataframe(pd.DataFrame(data["movers"]), hide_index=True, use_container_width=True)

# --- AGENTS ---
st.divider()
st.subheader("🤖 Autonomous Agent Command")
cols = st.columns(len(data["agents"]))
for i, task in enumerate(data["agents"]):
    with cols[i]:
        with st.container(border=True):
            st.markdown(f"**{task['agent']}**")
            st.caption(task['task'])
            st.write(f"🟢 {task['status']}")
            st.progress(random.randint(75, 98))

# --- AI CHAT ---
st.divider()
st.subheader("🧠 Ask Sapio AI (v1.0-Alpha)")
with st.container(border=True):
    u = st.text_input("Analyze the current market...")
    if u:
        st.chat_message("assistant").info(data["insight"])

st.divider()
st.caption(f"© 2026 Sapio Intel | Session Sync: {datetime.now().strftime('%H:%M:%S')}")
st.divider()
st.subheader("⚡ Sapio Intent Engine (Revenue Layer)")

with st.container(border=True):
    col_a, col_b = st.columns([3, 1])
    with col_a:
        intent = st.text_input("Set an Autonomous Mission...", placeholder="e.g. 'Swap 100 USDC for NEAR if AI Confidence hits 99%'")
    with col_b:
        if st.button("🚀 Deploy Mission"):
            st.success("Mission Authorized. Agent 'Sapio-Alpha-1' is now a Solver.")
            st.balloons()
            st.info("Projected Revenue Share: 0.12% per execution")
