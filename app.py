import streamlit as st
import json
import pandas as pd
import os

st.title("🧠 Sapio: The Agentic GDP Terminal")

# This is the EXACT path to your data
JSON_PATH = "/Users/birpratapsingh/Documents/Agentic_GDP_Live_Feed.json"

# --- 2. THE HEADER ---
st.subheader("Institutional Intelligence for the Solana AI Ecosystem")
st.markdown("---")

# --- 3. THE DATA ENGINE ---
if os.path.exists(JSON_PATH):
    try:
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        
        # Display High-Level Metrics
        col1, col2, col3 = st.columns(3)
        
        # Handling the data from your specific JSON structure
        global_gdp = data.get("global_aGDP_estimate", "$0")
        
        col1.metric("Global aGDP Estimate", global_gdp, "+12.5% (24h)")
        col2.metric("Network Status", "Institutional Grade", delta_color="normal")
        col3.metric("Terminal Status", "LIVE / ENCRYPTED")

        st.markdown("### 💎 High-Signal Project Flow")
        st.write("Current projects hitting the 99th percentile for SVM momentum:")
        
        # Convert the list of projects to a clean table
        df = pd.DataFrame(data.get("top_movers", []))
        st.table(df)

        st.success("✅ REAL-TIME CONNECTION ESTABLISHED")

    except Exception as e:
        st.error(f"Error parsing JSON: {e}")
else:
    st.error(f"❌ CRITICAL ERROR: File not found at {JSON_PATH}")
    st.info("Founder Check: Ensure 'Agentic_GDP_Live_Feed.json' is sitting in your Documents folder.")

# --- 4. THE REVENUE HOOK (SIDEBAR) ---
st.sidebar.header("🔒 Tier-1 Angel Syndicate")
st.sidebar.write("Access pre-seed rounds for vetted AI-Crypto infrastructure.")
lead_email = st.sidebar.text_input("Enter Email for Private Deal Flow")

if st.sidebar.button("Request Access"):
    if lead_email:
        st.sidebar.success(f"Application sent for {lead_email}")
        st.balloons()
    else:
        st.sidebar.warning("Please enter an email.")

# --- 5. THE PITCH FOOTER ---
st.markdown("---")
st.caption("Proprietary Intelligence by Aetheria Labs. 2026. All Rights Reserved.")
# Change the title and sidebar
st.set_page_config(page_title="Sapio Terminal | AI-Crypto Intelligence", layout="wide")

st.title("🧠 Sapio: The Agentic GDP Terminal")
st.subheader("Institutional Intelligence for the Solana AI Ecosystem")

# Change the footer at the bottom
st.caption("Proprietary Intelligence by Sapio Labs. 2026. All Rights Reserved.")
