import streamlit as st
import pandas as pd
import time

# --- SAPIO WEB INTERFACE v16.1 ---
st.set_page_config(page_title="Sapio Sovereign | Web Terminal", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #00ffcc; }
    .status-box { border: 1px solid #00ffcc; padding: 20px; border-radius: 5px; background: #0d1117; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ SAPIO SOVEREIGN TERMINAL")
st.caption("CONNECTED TO RUST KERNEL v16.0 | XRPL MAINNET")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🏦 Treasury Status")
    # This simulates pulling data from your Rust 'Engine'
    st.metric("Verified Revenue", "$0.0025", "PLATFORM FEE")
    st.metric("Agentic GDP", "$6.58B", "+0.01")
    
    st.divider()
    st.markdown("### 📜 Compliance Log")
    st.code("ISO 20022: pacs.008\nSTATUS: VALIDATED\nHASH: 8f9a...c32d", language="text")

with col2:
    st.markdown("### 🛰️ Live Mission Control")
    st.area_chart([6.50, 6.52, 6.55, 6.57, 6.58], color="#00ffcc")
    
    if st.button("EXECUTE MISSION (TRIGGER RUST)"):
        with st.status("Sending Intent to Rust Kernel..."):
            time.sleep(1)
            st.success("Mission Success: Check Rust Terminal for Hash")

st.divider()
st.caption("Sapio Intel Protocol | Built with Rust & Python")
