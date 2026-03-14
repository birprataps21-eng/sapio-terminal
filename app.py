import streamlit as st
import pandas as pd
import requests
import yfinance as yf
import plotly.express as px

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Sapio Intelligence Terminal",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------
# DARK TERMINAL UI
# ------------------------------------------------

st.markdown("""
<style>

body{
background-color:#0b0f19;
}

.top-banner{
background:linear-gradient(90deg,#111827,#1f2937);
padding:25px;
border-radius:12px;
text-align:center;
color:white;
font-size:22px;
font-weight:600;
margin-bottom:20px;
}

button{
border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.markdown("""
<div class="top-banner">
Sapio Institutional Intelligence Terminal — AI powered market analytics, real-time crypto data and global grant intelligence.
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# PAGE STATE
# ------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page="Markets"

page=st.session_state.page

# ------------------------------------------------
# NAVIGATION BAR
# ------------------------------------------------

col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

if col1.button("Markets"):
    st.session_state.page="Markets"

if col2.button("Stocks"):
    st.session_state.page="Stocks"

if col3.button("Crypto"):
    st.session_state.page="Crypto"

if col4.button("AI Insights"):
    st.session_state.page="AI"

if col5.button("Sentiment"):
    st.session_state.page="Sentiment"

if col6.button("Portfolio"):
    st.session_state.page="Portfolio"

if col7.button("Grants"):
    st.session_state.page="Grants"

if col8.button("Premium"):
    st.session_state.page="Premium"

st.divider()

# ------------------------------------------------
# SAFE CRYPTO API
# ------------------------------------------------

def get_crypto_price():

    url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

    try:

        response=requests.get(url,timeout=10)
        data=response.json()

        bitcoin=data.get("bitcoin",{}).get("usd","N/A")
        ethereum=data.get("ethereum",{}).get("usd","N/A")
        solana=data.get("solana",{}).get("usd","N/A")

        return {
            "Bitcoin":bitcoin,
            "Ethereum":ethereum,
            "Solana":solana
        }

    except:
        return {
            "Bitcoin":"API Error",
            "Ethereum":"API Error",
            "Solana":"API Error"
        }

# ------------------------------------------------
# MARKETS PAGE
# ------------------------------------------------

if page=="Markets":

    st.header("Real Time Crypto Prices")

    crypto=get_crypto_price()

    c1,c2,c3=st.columns(3)

    c1.metric("Bitcoin",crypto["Bitcoin"])
    c2.metric("Ethereum",crypto["Ethereum"])
    c3.metric("Solana",crypto["Solana"])

# ------------------------------------------------
# STOCK ANALYZER
# ------------------------------------------------

elif page=="Stocks":

    st.header("Stock Analyzer")

    ticker=st.text_input("Enter Stock Ticker","AAPL")

    try:

        data=yf.download(ticker,start="2023-01-01")

        if not data.empty:

            fig=px.line(data,x=data.index,y="Close",title=f"{ticker} Price")

            st.plotly_chart(fig,use_container_width=True)

            st.dataframe(data.tail())

        else:
            st.warning("No stock data found.")

    except:
        st.error("Stock API Error")

# ------------------------------------------------
# CRYPTO DASHBOARD
# ------------------------------------------------

elif page=="Crypto":

    st.header("Crypto Market Dashboard")

    crypto=get_crypto_price()

    st.metric("Bitcoin",crypto["Bitcoin"])
    st.metric("Ethereum",crypto["Ethereum"])
    st.metric("Solana",crypto["Solana"])

# ------------------------------------------------
# AI INSIGHTS
# ------------------------------------------------

elif page=="AI":

    st.header("AI Market Insights")

    st.info("AI analytics module coming soon")

# ------------------------------------------------
# SENTIMENT
# ------------------------------------------------

elif page=="Sentiment":

    st.header("Market Sentiment")

    st.info("Sentiment analytics coming soon")

# ------------------------------------------------
# PORTFOLIO TRACKER
# ------------------------------------------------

elif page=="Portfolio":

    st.header("Portfolio Tracker")

    asset=st.text_input("Asset")

    amount=st.number_input("Investment Amount")

    if st.button("Add Asset"):

        st.success(f"{asset} added with investment ${amount}")

# ------------------------------------------------
# GRANT DATABASE
# ------------------------------------------------

elif page=="Grants":

    st.header("Global Grant Database")

    try:

        df=pd.read_csv("grants.csv")

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

        if st.button("Find Grants"):

            matches=df[df["Region"].str.contains(region,case=False)]

            st.dataframe(matches.head(10))

    except:
        st.warning("grants.csv not found")

# ------------------------------------------------
# PREMIUM PAGE
# ------------------------------------------------

elif page=="Premium":

    st.header("Institutional Tools")

    st.write("Advanced funding analytics and intelligence tools for institutions.")
