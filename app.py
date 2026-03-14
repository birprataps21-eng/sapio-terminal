import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import numpy as np

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Sapio Intelligence Terminal",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# TERMINAL STYLE UI
# -------------------------------------------------

st.markdown("""
<style>

body {
    background-color:#0b0f19;
}

.top-banner{
background:linear-gradient(90deg,#111827,#1f2937);
padding:20px;
border-radius:10px;
margin-bottom:20px;
animation:fadeIn 2s ease-in;
}

.banner-text{
color:white;
font-size:22px;
font-weight:600;
text-align:center;
}

.sidebar .sidebar-content {
background-color:#0b0f19;
}

.stButton>button{
background-color:#2563eb;
color:white;
border-radius:8px;
}

@keyframes fadeIn{
from{opacity:0}
to{opacity:1}
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TOP BANNER
# -------------------------------------------------

st.markdown("""
<div class="top-banner">
<div class="banner-text">
Sapio Institutional Intelligence Terminal — Financial analytics, AI insights,
and a global grant discovery platform for startups, researchers, and institutions.
</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("Sapio Intelligence Terminal")

st.write(
"Professional institutional intelligence combining financial markets and grant funding data."
)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("Terminal Menu")

page = st.sidebar.radio(
"Navigate",
[
"Market Dashboard",
"Stock Analyzer",
"Crypto Dashboard",
"AI Market Insights",
"Sentiment Analysis",
"Portfolio Tracker",
"Grant Database",
"Premium Tools"
]
)

# -------------------------------------------------
# MARKET DASHBOARD
# -------------------------------------------------

if page == "Market Dashboard":

    st.header("Global Markets")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("S&P 500","5120","+1.2%")
    col2.metric("NASDAQ","16320","+0.8%")
    col3.metric("Bitcoin","$68200","+2.4%")
    col4.metric("Gold","$2150","+0.5%")

    data = px.data.stocks()

    fig = px.line(data,x="date",y=data.columns[1:],title="Market Trend")

    st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# STOCK ANALYZER
# -------------------------------------------------

elif page == "Stock Analyzer":

    st.header("Stock Analysis")

    ticker = st.text_input("Stock Ticker","AAPL")

    period = st.selectbox("Period",["1mo","3mo","6mo","1y","5y"])

    if st.button("Analyze"):

        stock = yf.download(ticker,period=period)

        fig = px.line(stock,x=stock.index,y="Close",title=f"{ticker} Price")

        st.plotly_chart(fig,use_container_width=True)

        st.dataframe(stock.tail(20))

# -------------------------------------------------
# CRYPTO DASHBOARD
# -------------------------------------------------

elif page == "Crypto Dashboard":

    st.header("Crypto Market")

    crypto_data = {
    "Coin":["Bitcoin","Ethereum","Solana","BNB"],
    "Price":[68200,3500,145,410],
    "Change %":[2.4,1.8,3.5,1.1]
    }

    df = pd.DataFrame(crypto_data)

    st.dataframe(df)

    fig = px.bar(df,x="Coin",y="Price",title="Crypto Prices")

    st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# AI INSIGHTS
# -------------------------------------------------

elif page == "AI Market Insights":

    st.header("AI Market Intelligence")

    if st.button("Generate Insight"):

        insights = [
        "AI sector attracting institutional capital.",
        "Crypto markets showing accumulation patterns.",
        "Technology sector outperforming global markets.",
        "Energy sector showing strong demand signals."
        ]

        st.success(np.random.choice(insights))

# -------------------------------------------------
# SENTIMENT
# -------------------------------------------------

elif page == "Sentiment Analysis":

    st.header("Market Sentiment")

    sentiment_data = {
    "Sector":["Technology","Energy","Finance","Healthcare"],
    "Sentiment":[0.78,0.62,0.55,0.48]
    }

    df = pd.DataFrame(sentiment_data)

    fig = px.bar(df,x="Sector",y="Sentiment",title="Sector Sentiment")

    st.plotly_chart(fig)

# -------------------------------------------------
# PORTFOLIO
# -------------------------------------------------

elif page == "Portfolio Tracker":

    st.header("Portfolio Tracker")

    ticker = st.text_input("Ticker")

    amount = st.number_input("Investment Amount")

    if st.button("Add Investment"):

        st.success(f"{ticker} added with value ${amount}")

# -------------------------------------------------
# GRANT DATABASE
# -------------------------------------------------

elif page == "Grant Database":

    st.header("Global Grant Intelligence Database")

    data = {
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
    ],

    "Region":[
    "Global",
    "US/EU",
    "Global",
    "EU",
    "US",
    "Global"
    ]
    }

    df = pd.DataFrame(data)

    category = st.selectbox(
    "Filter by Category",
    ["All","Startups","Artificial Intelligence","Technology","Climate","Healthcare","Small Business"]
    )

    if category != "All":
        df = df[df["Category"] == category]

    st.dataframe(df)

# -------------------------------------------------
# PREMIUM
# -------------------------------------------------

elif page == "Premium Tools":

    st.header("Institutional Premium Tools")

    st.warning("Upgrade required for advanced analytics")

    st.write("🔒 Institutional Flow Tracking")
    st.write("🔒 Hedge Fund Signals")
    st.write("🔒 AI Trading Models")
    st.write("🔒 Advanced Grant Intelligence")

    if st.button("Upgrade to Pro"):

        st.success("Crypto payment gateway coming soon.")
