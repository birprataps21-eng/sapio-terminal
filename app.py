import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sapio Intelligence Terminal", layout="wide")

# --- SIDEBAR ALPHA ALERTS ---
with st.sidebar:
    st.title("🛰️ Sapio Live Feed")
    st.status("XRPL x402 Node: ONLINE", state="complete")
    st.status("NEAR Sharding Node: ONLINE", state="complete")
    
    st.markdown("### **2026 Alpha Alerts**")
    st.info("**XRPL:** XAO DAO is now voting on AI microgrants.")
    st.warning("**NEAR:** DWF Labs launched a $20M AI Agent Fund.")
    st.divider()
    st.write("Built for the Agentic Future.")

# --- DATA LOADING ---
JSON_PATH = "Agentic_GDP_Live_Feed.json"

if os.path.exists(JSON_PATH):
    with open(JSON_PATH, "r") as f:
        data = json.load(f)
else:
    data = {"global_aGDP_estimate": "Loading...", "chains": [], "top_movers": []}

# --- MAIN DASHBOARD ---
st.title("🌐 Sapio Intelligence Terminal")
st.metric("Total Agentic GDP (Estimate)", data.get("global_aGDP_estimate", "$0"))

st.subheader("High-Signal Project Flow")
st.table(data.get("top_movers", []))

# --- REQUEST ACCESS FORM ---
st.markdown("---")
st.subheader("📩 Request Institutional API Access")
st.write("Join the waitlist for Sapio Intelligence alpha seats (H1 2026).")

with st.form("request_form"):
    email = st.text_input("Work Email Address")
    organization = st.selectbox("Organization Type", ["Venture Fund", "L1 Foundation", "Trading Desk", "Individual Builder"])
    submitted = st.form_submit_button("Request Access")
    
    if submitted:
        if "@" in email:
            st.success(f"✅ Request received for {email}. We will reach out shortly.")
        else:
            st.error("Please enter a valid email.")
