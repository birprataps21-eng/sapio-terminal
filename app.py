def load_all_data():
    # FORCE THE APP TO LOOK IN ITS OWN FOLDER
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gdp_path = os.path.join(current_dir, "Agentic_GDP_Live_Feed.json")
    news_path = os.path.join(current_dir, "Sapio_News_Feed.json")
    
    # Defaults if files are missing
    combined_data = {"gdp": {"global_aGDP_estimate": "$0.0B"}, "news": []}
    
    if os.path.exists(gdp_path):
        with open(gdp_path, "r") as f:
            combined_data["gdp"] = json.load(f)
    if os.path.exists(news_path):
        with open(news_path, "r") as f:
            combined_data["news"] = json.load(f)
            
    return combined_data
import streamlit as st
import json
import os
import random  # <--- FIXED: Added missing import
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sapio Intelligence | v3.8 AI", 
    page_icon="⚡", 
    layout="wide"
)

# --- 2. MODULAR DATA LOADING ---
def load_all_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gdp_path = os.path.join(current_dir, "Agentic_GDP_Live_Feed.json")
    news_path = os.path.join(current_dir, "Sapio_News_Feed.json")
    
    # Standard "Safe" data if files are missing or scraper hasn't run
    combined_data = {
        "gdp": {
            "global_aGDP_estimate": "$0.0B", 
            "top_movers": [], 
            "agent_tasks": [],
            "ai_insight": "Initializing AI Brain..."
        },
        "news": ["System Booting... Run scraper.py to populate feed."]
    }
    
    if os.path.exists(gdp_path):
        with open(gdp_path, "r") as f:
            combined_data["gdp"] = json.load(f)
            
    if os.path.exists(news_path):
        with open(news_path, "r") as f:
            combined_data["news"] = json.load(f)
            
    return combined_data

data = load_all_data()

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/radar.png", width=60)
    st.title("Sapio Command")
    st.status("XRPL x402 Node: ONLINE", state="complete")
    st.status("NEAR Sharding: OPTIMIZED", state="complete")
    st.divider()
    st.markdown("### 🛰️ Whale Watcher")
    st.caption(f"**{datetime.now().strftime('%H:%M')}** | 1.2M XRP → Institutional Custody")
    st.caption(f"**{datetime.now().strftime('%H:%M')}** | 45k NEAR → AI Compute Pool")

# --- 4. MAIN TERMINAL UI ---
st.title("🌐 Sapio Intelligence Terminal")
st.markdown("### `System Status: AI INTEGRATED GOD MODE`")

# --- 5. THE BLOOMBERG TICKER ---
news_string = " • ".join(data["news"])
st.markdown(f"""
    <div style="background-color: #0e1117; padding: 12px; border-radius: 10px; border: 1px solid #00ffcc; box-shadow: 0px 0px 10px #00ffcc;">
        <marquee behavior="scroll" direction="left" style="color: #00ffcc; font-family: 'Courier New', monospace; font-size: 1.1rem; font-weight: bold;">
            [LIVE ALPHA FEED] • {news_string}
        </marquee>
    </div>
""", unsafe_allow_html=True)
st.write("") 

# --- 6. TOP LEVEL METRICS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Agentic GDP", data["gdp"].get("global_aGDP_estimate", "$6.4B"), "+14.2%")
m2.metric("XRPL Standard", "ISO-20022", "Active")
m3.metric("NEAR Nodes", "14,802", "+402")
m4.metric("AI Confidence", "98.4%", "Optimal")

# --- 7. AGENTIC COMMAND CENTER ---
st.divider()
st.subheader("🤖 Autonomous Agent Command")
agent_tasks = data["gdp"].get("agent_tasks", [])

if agent_tasks:
    agent_cols = st.columns(len(agent_tasks))
    for i, task in enumerate(agent_tasks):
        with agent_cols[i]:
            with st.container(border=True):
                st.markdown(f"**{task['agent']}**")
                st.caption(task['task'])
                status_icon = "🟢" if task['status'] == "ACTIVE" else "🔵"
                st.write(f"{status_icon} {task['status']}")
                # Using random now that it is imported!
                val = random.randint(40, 95) if task['status'] == "ACTIVE" else 100
                st.progress(val)
else:
    st.info("No active agents found. Run scraper.py to deploy.")

# --- 8. SAPIO AI: THE BRAIN LAYER ---
st.divider()
st.subheader("🧠 Ask Sapio AI (v1.0-Alpha)")

with st.container(border=True):
    user_query = st.text_input("Analyze the current agentic market for me...", placeholder="e.g., Should I focus on XRPL or NEAR?")
    
    if user_query:
        with st.spinner("Sapio AI is analyzing on-chain clusters..."):
            insight = data["gdp"].get("ai_insight", "Data currently being indexed...")
            st.chat_message("assistant").write(f"**Analysis for:** '{user_query}'")
            st.chat_message("assistant").info(insight)

# --- 9. INSTITUTIONAL PRO FOOTER ---
st.divider()
st.subheader("💎 Sapio Institutional Pro")
footer_col1, footer_col2 = st.columns([2, 1])

with footer_col1:
    st.write("Unlock the **XRPL x402 Deep-Liquidity Feed** and **NEAR Agentic Sentiment API**.")
    st.info("Institutional Tier: $499/mo | Alpha Individual: $49/mo")

with footer_col2:
    if st.button("🚀 Upgrade to Pro"):
        st.success("Redirecting to Sapio Secure Gateway...")
        st.snow()
        st.markdown("""
        **PRO FEATURES UNLOCKED (PREVIEW):**
        - • Real-time DWF Labs Portfolio Tracker
        - • XAO DAO Governance Prediction Engine
        - • Priority Support via Private Discord
        """)

st.divider()
st.caption(f"© 2026 Sapio Intel | Last Sync: {datetime.now().strftime('%H:%M:%S')} | Restricted Access")
