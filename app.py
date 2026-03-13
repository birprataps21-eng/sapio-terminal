import streamlit as st
import json
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sapio Intelligence Terminal", 
    page_icon="🌐", 
    layout="wide"
)

# --- 2. THE INSTITUTIONAL SIDEBAR ---
with st.sidebar:
    st.title("🛰️ Sapio Live Feed")
    st.status("XRPL x402 Node: ONLINE", state="complete")
    st.status("NEAR Sharding Node: ONLINE", state="complete")
    
    st.markdown("### **March 2026 Alpha Alerts**")
    st.info("**XRPL:** XAO DAO is now voting on AI-agent microgrants.")
    st.warning("**NEAR:** DWF Labs launched a $20M AI Agent Fund.")
    
    st.divider()
    st.caption("Sapio Core v2.0.4 | Secure Connection")

# --- 3. BULLETPROOF DATA LOADING ---
def load_data():
    # Looks for the JSON file in the same folder as this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "Agentic_GDP_Live_Feed.json")
    
    # Fallback for Streamlit Cloud
    if not os.path.exists(json_path):
        json_path = "Agentic_GDP_Live_Feed.json"

    if os.path.exists(json_path):
        try:
            with open(json_path, "r") as f:
                return json.load(f)
        except Exception as e:
            return {"error": f"Read Error: {e}"}
    return None

data = load_data()

# --- 4. MAIN DASHBOARD UI ---
st.title("🌐 Sapio Intelligence Terminal")
st.markdown("#### *Real-Time Institutional Agentic GDP Tracker*")

if data and "error" not in data:
    # Top Level Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Agentic GDP (Estimate)", data.get("global_aGDP_estimate", "$0"))
    with col2:
        st.metric("Active AI Agents", "12,402", "+8% (24h)")
    with col3:
        st.metric("Settlement Standard", "ISO-20022 / x402")

    # Data Table
    st.subheader("High-Signal Project Flow (XRPL & NEAR)")
    st.table(data.get("top_movers", []))
    
else:
    # Error state if JSON is missing
    st.error("⚠️ DATA SYNC ERROR: Cannot find 'Agentic_GDP_Live_Feed.json'.")
    st.info("Run your scraper.py first to generate the data file.")

# --- 5. REQUEST ACCESS FORM ---
st.divider()
st.subheader("📩 Request Institutional API Access")

with st.form("request_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        email = st.text_input("Professional Email")
    with col_b:
        org = st.selectbox("Organization", ["Venture Fund", "L1 Foundation", "Trading Desk", "Research Lab"])
    
    submitted = st.form_submit_button("Submit Application")
    
    if submitted:
        if "@" in email:
            st.success(f"✅ Application received for {email}.")
        else:
            st.error("Please enter a valid email.")

st.caption("© 2026 Sapio Intelligence.")
