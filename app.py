import streamlit as st
import json
import os
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sapio Intelligence | v3.7", 
    page_icon="⚡", 
    layout="wide"
)

# --- 2. MODULAR DATA LOADING ---
def load_all_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gdp_path = os.path.join(current_dir, "Agentic_GDP_Live_Feed.json")
    news_path = os.path.join(current_dir, "Sapio_News_Feed.json")
    
    combined_data = {
        "gdp": {"global_aGDP_estimate": "$0.0B", "top_movers": []},
        "news": ["System Booting... Run scraper.py to populate."]
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
    st.caption("**14:22** | 1.2M XRP → Institutional Custody")
    st.caption("**14:15** | 45k NEAR → AI Compute Pool")

# --- 4. MAIN TERMINAL UI ---
st.title("🌐 Sapio Intelligence Terminal")
st.markdown("### `System Status: GOD MODE ACTIVATED`")

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
m4.metric("Alpha Signal", "CRITICAL", "High")

# --- 7. ECOSYSTEM DATA ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📊 High-Signal Project Flow")
    if data["gdp"].get("top_movers"):
        st.table(data["gdp"]["top_movers"])
    else:
        st.info("Run scraper.py to view data.")

with col_right:
    st.subheader("📩 API Beta Access")
    with st.container(border=True):
        email = st.text_input("Professional Email")
        if st.button("Request Alpha Access"):
            st.balloons()
            st.success("Added to Institutional Waitlist.")

# --- 8. THE FOOTER (Institutional Pro Upgrade) ---
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
