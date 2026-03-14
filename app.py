import streamlit as st
import pandas as pd
import yfinance as yf
import requests
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Sapio Intelligence Terminal",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# DARK TERMINAL STYLE
# --------------------------------------------------

st.markdown("""
<style>

body {
background-color:#0b0f19;
}

.top-banner{
background:linear-gradient(90deg,#111827,#1f2937);
padding:25px;
border-radius:12px;
margin-bottom:20px;
text-align:center;
color:white;
font-size:22px;
font-weight:600;
}

.metric-box{
background:#111827;
padding:15px;
border-radius:10px;
text-align:center;
color:white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TOP BANNER
# --------------------------------------------------

st.markdown("""
<div class="top-banner">
Sapio Institutional Intelligence Terminal — Markets, Crypto Analytics, and Global Grant Intelligence
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PAGE STATE
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Market Dashboard"

page = st.session_state.page

# --------------------------------------------------
# NAVIGATION BUTTONS
# --------------------------------------------------

col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

if col1.button("Markets"):
    st.session_state.page="Market Dashboard"

if col2.button("Stocks"):
    st.session_state.page="Stock Analyzer"

if col3.button("Crypto"):
    st.session_state.page="Crypto Dashboard"

if col4.button("AI"):
    st.session_state.page="AI Insights"

if col5.button("Sentiment"):
    st.session_state.page="Sentiment Analysis"

if col6.button("Portfolio"):
    st.session_state.page="Portfolio Tracker"

if col7.button("Grants"):
    st.session_state.page="Grant Database"

if col8.button("Premium"):
    st.session_state.page="Premium Tools"

st.divider()

# --------------------------------------------------
# API FUNCTIONS
# --------------------------------------------------

def get_crypto_price():

    url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

    data=requests.get(url).json()

    return {
        "Bitcoin":data["bitcoin"]["usd"],
        "Ethereum":data["ethereum"]["usd"],
        "Solana":data["solana"]["usd"]
    }

# --------------------------------------------------
# MARKET DASHBOARD
# --------------------------------------------------

if page=="Market Dashboard":

    st.header("Global Market Overview")

    crypto=get_crypto_price()

    c1,c2,c3=st.columns(3)

    c1.metric("Bitcoin Price",crypto["Bitcoin"])
    c2.metric("Ethereum Price",crypto["Ethereum"])
    c3.metric("Solana Price",crypto["Solana"])

# --------------------------------------------------
# STOCK ANALYZER
# --------------------------------------------------

elif page=="Stock Analyzer":

    st.header("Stock Market Analyzer")

    ticker=st.text_input("Enter Stock Ticker","AAPL")

    if ticker:

        data=yf.download(ticker,start="2023-01-01")

        st.line_chart(data["Close"])

        st.dataframe(data.tail())

# --------------------------------------------------
# CRYPTO DASHBOARD
# --------------------------------------------------

elif page=="Crypto Dashboard":

    st.header("Crypto Market Dashboard")

    crypto=get_crypto_price()

    st.metric("Bitcoin",crypto["Bitcoin"])
    st.metric("Ethereum",crypto["Ethereum"])
    st.metric("Solana",crypto["Solana"])

# --------------------------------------------------
# AI MARKET INSIGHTS
# --------------------------------------------------

elif page=="AI Insights":

    st.header("AI Market Insights")

    st.info("AI analytics module coming soon")

# --------------------------------------------------
# SENTIMENT ANALYSIS
# --------------------------------------------------

elif page=="Sentiment Analysis":

    st.header("Market Sentiment")

    st.info("Sentiment analytics module coming soon")

# --------------------------------------------------
# PORTFOLIO TRACKER
# --------------------------------------------------

elif page=="Portfolio Tracker":

    st.header("Portfolio Tracker")

    ticker=st.text_input("Add Asset","AAPL")

    amount=st.number_input("Investment Amount")

    if st.button("Add to Portfolio"):

        st.success("Asset added to portfolio")

# --------------------------------------------------
# GRANT DATABASE
# --------------------------------------------------

elif page=="Grant Database":

    st.header("Global Grant Database")

    try:
        df=pd.read_csv("grants.csv")
    except:
        st.warning("grants.csv not found. Add your grant database file.")
        df=pd.DataFrame()

    if not df.empty:

        st.dataframe(df)

        st.subheader("Grant Eligibility Checker")

        industry=st.selectbox(
            "Industry",
            ["AI","Technology","Healthcare","Climate","General"]
        )

        region=st.selectbox(
            "Region",
            ["US","EU","Global"]
        )

        funding=st.number_input("Minimum Funding Needed")

        if st.button("Find Matching Grants"):

            matches=df[df["Region"].str.contains(region,case=False)]

            st.dataframe(matches.head(10))

# --------------------------------------------------
# PREMIUM TOOLS
# --------------------------------------------------

elif page=="Premium Tools":

    st.header("Premium Institutional Tools")

    st.write("Advanced analytics for institutions and grant intelligence.")

