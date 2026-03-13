import streamlit as st
import json
import os
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sapio Intelligence | v3.1 God Mode", 
    page_icon="⚡", 
    layout="wide"
)

# --- 2. MODULAR DATA LOADING ---
def load_all_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gdp_path = os.path.join(current_dir, "Agentic_GDP_Live_Feed.json")
    news_path = os.path.join(current_dir, "Sapio_News_Feed.json")
    
    # Initialize with default "Safe" data in case files are missing
    combined_data = {
        "gdp": {"global_aGDP_estimate": "$6.2B", "top_movers": []},
        "news": ["System initializing...", "Scanning XRPL & NEAR nodes..."]
    }
    
    # Load GDP Data
    if os.path.exists(gdp_path):
        try:
            with open(gdp_path, "r") as f:
                combined_data["gdp"] = json.load(f)
        except: pass
            
    # Load News Data
    if os.path.exists(news_path):
        try:
            with open(news_path, "r") as f:
                combined_data["news"] = json.load(f)
        except: pass
            
    return combined_data

data = load_all_data()

# --- 3. INSTITUTIONAL SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/ffffff/radar.png", width=60)
    st.title("Sapio Command")
    st.status("XRPL x402 Node: ONLINE", state="complete")
    st.status("NEAR Sharding: OPTIMIZED", state="complete")
    
    st.divider()
    st.markdown("### 🛰️ Whale Watcher (Live)")
    # High-signal simulated whale alerts for institutional feel
    st.caption("**14:22** | 1.2M XRP → Institutional Custody")
    st.caption("**14:15** | 45k NEAR → AI Compute Pool")
    st.caption("**13:58** | 800k XRP → x402 Settlement")
    
    st.divider()
    st.caption(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")

# --- 4. MAIN TERMINAL UI ---
st.title("🌐 Sapio Intelligence Terminal")
st.markdown("### `System Status: GOD MODE ACTIVATED`")

# --- 5. THE BLOOMBERG TICKER ---
# This converts your news list into one long scrolling string
news_string = " • ".join(data["news"])
st.markdown(f"""
    <div style="background-color: #0e1117; padding: 12px; border-radius: 10px; border: 1px solid #00ffcc; box-shadow: 0px 0px 10px #00ffcc;">
        <marquee behavior="scroll" direction="left" style="color: #00ffcc; font-family: 'Courier New', monospace; font-size: 1.1rem; font-weight: bold;">
            [LIVE ALPHA FEED] • {news_string} • Deploying Sapio v3.1...
        </marquee>
    </div>
""", unsafe_allow_html=True)
st.write("") 

# --- 6. TOP LEVEL METRICS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Agentic GDP", data["gdp"].get("global_aGDP_estimate", "$6.2B"), "+14.2%")
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
        st.info("Waiting for scraper to populate movement data...")

with col_right:
    st.subheader("📩 API Beta Access")
    with st.container(border=True):
        st.write("Join the Institutional Waitlist")
        email = st.text_input("Professional Email")
        org = st.selectbox("Organization", ["Venture Fund", "L1 Foundation", "Trading Desk"])
        if st.button("Request Alpha Access"):
            if "@" in email:
                st.balloons()
                st.success("Application Submitted.")
            else:
                st.error("Invalid Email.")

# --- 8. FOOTER ---
st.divider()
st.caption("© 2026 Sapio Intelligence | Powered by XRPL & NEAR Protocol | Authorized Personnel Only")
