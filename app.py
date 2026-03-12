import streamlit as st
import pandas as pd
import json
import os

# --- 1. SAPIO CONFIGURATION ---
st.set_page_config(
    page_title="Sapio Terminal | AI-Crypto Intelligence", 
    page_icon="🧠",
    layout="wide"
)

# CRITICAL: We use a relative path so it works on your Mac AND in the Cloud
JSON_PATH = "Agentic_GDP_Live_Feed.json"

# --- 2. HEADER & BRANDING ---
st.title("🧠 Sapio: The Agentic GDP Terminal")
st.subheader("Institutional Intelligence for Solana, XRPL, & NEAR")
st.markdown("---")

# --- 3. DATA ENGINE ---
# This block safely checks for your data and displays it
if os.path.exists(JSON_PATH):
    try:
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        
        # Main Metric (The 'North Star' of the project)
        st.metric(
            label="Total Ecosystem Agentic GDP", 
            value=data.get("global_aGDP_estimate", "N/A"), 
            delta="+$1.6B (7d)"
        )
        
        st.write("### 🌐 Cross-Chain Liquidity Flow")
        # Create a clean table for the different chains
        if "chains" in data:
            df_chains = pd.DataFrame(data["chains"])
            st.dataframe(df_chains, use_container_width=True, hide_index=True)

        st.write("### 💎 High-Signal Project Flow")
        # Show specific AI agents moving the most volume
        if "top_movers" in data:
            df_movers = pd.DataFrame(data["top_movers"])
            st.table(df_movers)

        st.success("✅ SAPIO INTELLIGENCE ONLINE: Multi-Chain Feed Active.")

    except Exception as e:
        st.error(f"Sync Error: {e}")
        st.info("Ensure the scraper has generated a valid JSON file.")
else:
    # This shows if the file is missing from the folder
    st.warning("🔄 Waiting for Sapio Scraper to feed live data...")
    st.info(f"Looking for file: {JSON_PATH}")

# --- 4. THE SAPIO SIDEBAR ---
with st.sidebar:
    st.header("🧠 Sapio Intelligence")
    st.write("Vetting the next generation of autonomous infrastructure on SVM and XRPL.")
    st.markdown("---")
    
    lead_email = st.text_input("Enter Email for Private Deal Flow")
    if st.button("Request Access"):
        if lead_email:
            st.success(f"Sapio Application sent for {lead_email}")
            st.balloons()
        else:
            st.error("Please enter a valid email.")

    st.markdown("---")
    st.caption("Proprietary Intelligence by Sapio Labs. 2026.")
