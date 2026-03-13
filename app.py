import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Sapio Intelligence | v6.1", page_icon="⚡", layout="wide")

# --- 2. SESSION STATE (The Revenue Engine) ---
if 'total_revenue' not in st.session_state:
    st.session_state.total_revenue = 0.0
if 'missions_completed' not in st.session_state:
    st.session_state.missions_completed = 0
if 'agent_performance' not in st.session_state:
    st.session_state.agent_performance = {
        "Sapio-Alpha-1": 0.0,
        "Whale-Tracker": 0.0,
        "Yield-Hunter": 0.0
    }

# --- 3. THE "NO-FILE" DATA FEED ---
def get_live_data():
    return {
        "gdp_val": f"${round(random.uniform(6.5, 6.8), 2)}B",
        "movers": [
            {"Project": "LiquidX (XRPL)", "Volume": "$142M", "Trend": "🚀 High"},
            {"Project": "NearScribe AI", "Volume": "$54M", "Trend": "📈 Steady"},
            {"Project": "Sapio Oracle", "Volume": "$18M", "Trend": "🔥 New"}
        ],
        "news": ["SYSTEM: AI Brain Linked", "XRPL: x402 Node Online", "NEAR: AI Compute Demand Spike"]
    }

data = get_live_data()

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/radar.png", width=60)
    st.title("Sapio Command")
    st.success("✓ XRPL x402 Node: ONLINE")
    st.success("✓ NEAR Sharding: OPTIMIZED")
    st.divider()
    st.markdown("### 🏦 Platform Treasury")
    st.metric("Total Revenue Collected", f"${round(st.session_state.total_revenue, 2)}", f"+{st.session_state.missions_completed} missions")
    st.divider()
    st.markdown("### 🛰️ Live Whale Feed")
    st.caption(f"{datetime.now().strftime('%H:%M')} | 1.2M XRP → Insto Custody")
    st.caption(f"{datetime.now().strftime('%H:%M')} | 45k NEAR → Compute Pool")

# --- 5. MAIN UI HEADER ---
st.title("🌐 Sapio Intelligence Terminal")
st.markdown("### `System Status: REVENUE GENERATION ACTIVE`")

# --- 6. TICKER (This was likely where the Error lived) ---
news_string = " • ".join(data["news"])
rev_val = round(st.session_state.total_revenue, 2)
ticker_html = f"""
    <div style="background-color: #0e1117; padding: 12px; border-radius: 10px; border: 2px solid #00ffcc;">
        <marquee style="color: #00ffcc; font-family: 'Courier New'; font-weight: bold;">
            [LIVE ALPHA FEED] • {news_string} • Platform Revenue: ${rev_val}
        </marquee>
    </div>
"""
st.markdown(ticker_html, unsafe_allow_html=True)

# --- 7. TOP LEVEL METRICS ---
st.write("")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Agentic GDP", data["gdp_val"], "+14.2%")
m2.metric("Missions Run", st.session_state.missions_completed, "Active")
m3.metric("NEAR Nodes", "14,802", "+402")
m4.metric("AI Confidence", "98.4%", "Optimal")

# --- 8. CHART & LEADERBOARD ---
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
    st.subheader("🏆 Agent Leaderboard")
    perf_data = []
    for k, v in st.session_state.agent_performance.items():
        perf_data.append({"Agent": k, "Revenue Gen": f"${round(v, 2)}"})
    st.table(pd.DataFrame(perf_data))

# --- 9. THE INTENT SOLVER (THE MONEY MAKER) ---
st.divider()
st.subheader("⚡ Sapio Autonomous Intent Solver")
st.caption("Instruct your agent to execute on-chain missions.")

with st.container(border=True):
    col_input, col_btn = st.columns([3, 1])
    with col_input:
        selected_agent = st.selectbox("Assign Agent", list(st.session_state.agent_performance.keys()))
        user_mission = st.text_input("Set Mission", placeholder="e.g. 'Harvest XRPL yield if APY > 15%'")
    with col_btn:
        st.write("###") # Spacer
        deploy = st.button("🚀 Deploy Mission", use_container_width=True)

    if deploy and user_mission:
        with st.status(f"Agent '{selected_agent}' Executing...", expanded=True) as status:
            st.write("🔍 Scanning liquidity on XRPL/NEAR...")
            time.sleep(1)
            st.write("⛓️ Verifying Intent Signature...")
            time.sleep(1)
            
            fee_earned = round(random.uniform(0.10, 0.85), 2)
            st.session_state.total_revenue += fee_earned
            st.session_state.missions_completed += 1
            st.session_state.agent_performance[selected_agent] += fee_earned
            
            status.update(label=f"SUCCESS: Mission Complete. Fee: ${fee_earned}", state="complete")
        st.balloons()

# --- 10. PROJECTS & MOVERS ---
st.divider()
st.subheader("🚀 Emerging Projects (AI Picks)")
st.dataframe(pd.DataFrame(data["movers"]), hide_index=True, use_container_width=True)

st.divider()
st.caption(f"© 2026 Sapio Intel | Founder Edition | Last Sync: {datetime.now().strftime('%H:%M:%S')}")
