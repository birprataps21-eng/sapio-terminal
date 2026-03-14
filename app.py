import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import numpy as np
import requests

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Sapio Intelligence Terminal",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------
# TERMINAL STYLE UI
# ------------------------------------------------

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
animation: fadeIn 1.5s ease-in;
}

.menu-container{
display:flex;
justify-content:center;
gap:10px;
margin-bottom:30px;
}

div.stButton > button{
background-color:#1f2937;
color:white;
border-radius:8px;
padding:10px 18px;
font-weight:600;
}

@keyframes fadeIn{
from{opacity:0}
to{opacity:1}
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# TOP BANNER
# ------------------------------------------------

st.markdown("""
<div class="top-banner">
Sapio Institutional Intelligence Terminal — AI powered market analytics,
real-time crypto data, and global grant intelligence for institutions,
researchers, and startups.
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# PAGE STATE
# ------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Market Dashboard"

# ------------------------------------------------
# TOP MENU BUTTONS
# ------------------------------------------------

col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

if col1.button("Markets"):
    st.session_state.page="Market Dashboard"

if col2.button("Stocks"):
    st.session_state.page="Stock Analyzer"

if col3.button("Crypto"):
    st.session_state.page="Crypto Dashboard"

if col4.button("AI Insights"):
    st.session_state.page="AI Market Insights"

if col5.button("Sentiment"):
    st.session_state.page="Sentiment Analysis"

if col6.button("Portfolio"):
    st.session_state.page="Portfolio Tracker"

if col7.button("Grants"):
    st.session_state.page="Grant Database"

if col8.button("Premium"):
    st.session_state.page="Premium Tools"

page = st.session_state.page

# ------------------------------------------------
# REAL-TIME CRYPTO DATA
# ------------------------------------------------

def get_crypto_price():

    url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

    data=requests.get(url).json()

    return {
        "Bitcoin":data["bitcoin"]["usd"],
        "Ethereum":data["ethereum"]["usd"],
        "Solana":data["solana"]["usd"]
    }

# ------------------------------------------------
# MARKET DASHBOARD
# ------------------------------------------------

if page=="Market Dashboard":

    st.header("Global Markets")

    crypto = get_crypto_price()

    col1,col2,col3 = st.columns(3)

    col1.metric("Bitcoin",f"${crypto['Bitcoin']}")
    col2.metric("Ethereum",f"${crypto['Ethereum']}")
    col3.metric("Solana",f"${crypto['Solana']}")

    st.subheader("Market Trend")

    data = px.data.stocks()

    fig = px.line(data,x="date",y=data.columns[1:],title="Global Market Trend")

    st.plotly_chart(fig,use_container_width=True)

# ------------------------------------------------
# STOCK ANALYZER
# ------------------------------------------------

elif page=="Stock Analyzer":

    st.header("Stock Analysis Terminal")

    ticker = st.text_input("Stock Ticker","AAPL")

    period = st.selectbox("Period",["1mo","3mo","6mo","1y","5y"])

    if st.button("Analyze"):

        stock = yf.download(ticker,period=period)

        fig = px.line(stock,x=stock.index,y="Close",title=f"{ticker} Price")

        st.plotly_chart(fig,use_container_width=True)

        st.dataframe(stock.tail(20))

# ------------------------------------------------
# CRYPTO DASHBOARD
# ------------------------------------------------

elif page=="Crypto Dashboard":

    st.header("Real Time Crypto Prices")

    crypto = get_crypto_price()

    df = pd.DataFrame({
        "Coin":crypto.keys(),
        "Price":crypto.values()
    })

    st.dataframe(df)

    fig = px.bar(df,x="Coin",y="Price",title="Crypto Prices")

    st.plotly_chart(fig,use_container_width=True)

# ------------------------------------------------
# AI INSIGHTS
# ------------------------------------------------

elif page=="AI Market Insights":

    st.header("AI Market Intelligence")

    if st.button("Generate Insight"):

        insights=[
        "Institutional demand rising in AI sector.",
        "Crypto accumulation phase detected.",
        "Tech equities outperforming macro markets.",
        "Energy sector gaining hedge fund inflows."
        ]

        st.success(np.random.choice(insights))

# ------------------------------------------------
# SENTIMENT ANALYSIS
# ------------------------------------------------

elif page=="Sentiment Analysis":

    st.header("Market Sentiment")

    sentiment_data={
    "Sector":["Technology","Energy","Finance","Healthcare"],
    "Sentiment":[0.78,0.62,0.55,0.48]
    }

    df=pd.DataFrame(sentiment_data)

    fig=px.bar(df,x="Sector",y="Sentiment",title="Sector Sentiment")

    st.plotly_chart(fig)

# ------------------------------------------------
# PORTFOLIO TRACKER
# ------------------------------------------------

elif page=="Portfolio Tracker":

    st.header("Portfolio Tracker")

    ticker = st.text_input("Ticker")

    amount = st.number_input("Investment Amount")

    if st.button("Add Investment"):

        st.success(f"{ticker} added with ${amount}")

# ------------------------------------------------
# GRANT DATABASE
# ------------------------------------------------

elif page=="Grant Database":

    st.header("Global Grant Intelligence Database")

    data={
    "Grant":[
    "Startup Innovation Grant",
    "AI Research Grant",
    "Tech Development Fund",
    "Climate Innovation Grant",
    "Healthcare Research Grant",
    "Small Business Expansion Fund"
    ],

    "Funding":[
    "$10k-$50k",
    "$50k-$200k",
    "$25k-$100k",
    "$100k-$500k",
    "$75k-$300k",
    "$20k-$80k"
    ],

    "Category":[
    "Startups",
    "Artificial Intelligence",
    "Technology",
    "Climate",
    "Healthcare",
    "Small Business"
    ]
    }

    df=pd.DataFrame(data)

    category=st.selectbox(
    "Filter Category",
    ["All","Startups","Artificial Intelligence","Technology","Climate","Healthcare","Small Business"]
    )

    if category!="All":
        df=df[df["Category"]==category]

    st.dataframe(df)

# ------------------------------------------------
# PREMIUM
# ------------------------------------------------

elif page=="Premium Tools":

    st.header("Institutional Premium Tools")

    st.warning("Crypto payments coming soon")

    st.write("🔒 Institutional Flow Tracking")
    st.write("🔒 Hedge Fund Signals")
    st.write("🔒 AI Trading Models")
    st.write("🔒 Advanced Grant Intelligence")

    if st.button("Upgrade"):

        st.success("Crypto payment integration coming soon.")
