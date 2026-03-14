import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import numpy as np

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Sapio Institutional Intelligence",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# PROFESSIONAL CSS + ANIMATION
# -------------------------------------------------

st.markdown("""
<style>

body {
    background-color:#0e1117;
}

.top-banner {
    width:100%;
    padding:20px;
    background:linear-gradient(90deg,#111827,#1f2937);
    border-radius:10px;
    margin-bottom:20px;
    animation: fadeIn 2s ease-in;
}

.banner-text {
    font-size:22px;
    font-weight:600;
    color:white;
    text-align:center;
}

@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}

.metric-box {
    background-color:#1c1f26;
    padding:10px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# ANIMATED TOP BANNER
# -------------------------------------------------

st.markdown("""
<div class="top-banner">
<div class="banner-text">
🚀 Sapio Institutional Intelligence — A professional terminal providing 
AI-powered market analysis, institutional tools, and a global grant discovery system 
for startups, researchers, and organizations seeking funding.
</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("📊 Sapio Finance & Grants Terminal")

st.write(
"Professional intelligence platform combining financial analytics, AI insights, and grant discovery."
)

# -------------------------------------------------
# SIDEBAR NAVIGATION
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
        "Grant Finder",
        "Premium Tools"
    ]
)

# -------------------------------------------------
# MARKET DASHBOARD
# -------------------------------------------------

if page == "Market Dashboard":

    st.header("Global Market Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("S&P 500","5120","+1.2%")
    col2.metric("NASDAQ","16320","+0.8%")
    col3.metric("Bitcoin","$68200","+2.4%")
    col4.metric("Gold","$2150","+0.5%")

    st.subheader("Market Trends")

    data = px.data.stocks()

    fig = px.line(
        data,
        x="date",
        y=data.columns[1:],
        title="Global Market Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# STOCK ANALYZER
# -------------------------------------------------

elif page == "Stock Analyzer":

    st.header("Stock Analysis Tool")

    ticker = st.text_input("Enter Stock Ticker","AAPL")

    period = st.selectbox(
        "Select Time Period",
        ["1mo","3mo","6mo","1y","5y"]
    )

    if st.button("Analyze Stock"):

        stock = yf.download(ticker,period=period)

        fig = px.line(
            stock,
            x=stock.index,
            y="Close",
            title=f"{ticker} Price Chart"
        )

        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Recent Data")

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

    fig = px.bar(
        df,
        x="Coin",
        y="Price",
        title="Crypto Market Prices"
    )

    st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# AI MARKET INSIGHTS
# -------------------------------------------------

elif page == "AI Market Insights":

    st.header("AI Market Intelligence")

    st.write("Generate AI-based market observations.")

    if st.button("Generate AI Insight"):

        insights = [
            "Technology sector showing strong institutional accumulation.",
            "Crypto markets entering bullish consolidation.",
            "AI companies outperforming major indices.",
            "Energy sector attracting hedge fund capital."
        ]

        st.success(np.random.choice(insights))

# -------------------------------------------------
# SENTIMENT ANALYSIS
# -------------------------------------------------

elif page == "Sentiment Analysis":

    st.header("Market Sentiment Analysis")

    sentiment_data = {
        "Sector":["Technology","Energy","Finance","Healthcare"],
        "Sentiment Score":[0.78,0.62,0.55,0.48]
    }

    df = pd.DataFrame(sentiment_data)

    fig = px.bar(
        df,
        x="Sector",
        y="Sentiment Score",
        title="Sector Sentiment"
    )

    st.plotly_chart(fig)

# -------------------------------------------------
# PORTFOLIO TRACKER
# -------------------------------------------------

elif page == "Portfolio Tracker":

    st.header("Investment Portfolio")

    ticker = st.text_input("Ticker Symbol")

    amount = st.number_input("Investment Amount")

    if st.button("Add Investment"):

        st.success(f"Added {ticker} investment worth ${amount}")

# -------------------------------------------------
# GRANT FINDER
# -------------------------------------------------

elif page == "Grant Finder":

    st.header("Startup & Research Grant Finder")

    st.write(
    "Search potential funding opportunities for startups, researchers, and institutions."
    )

    grants = {
        "Grant Name":[
            "Startup Innovation Grant",
            "Technology Development Fund",
            "AI Research Grant",
            "Small Business Growth Grant"
        ],

        "Funding Amount":[
            "$10k-$50k",
            "$25k-$100k",
            "$50k-$200k",
            "$20k-$80k"
        ],

        "Category":[
            "Startups",
            "Technology",
            "Artificial Intelligence",
            "Small Business"
        ]
    }

    df = pd.DataFrame(grants)

    st.dataframe(df)

    industry = st.selectbox(
        "Select Industry",
        [
            "Technology",
            "Healthcare",
            "AI",
            "Finance",
            "Education"
        ]
    )

    if st.button("Find Grants"):

        st.success(f"Showing grant opportunities for {industry} sector.")

# -------------------------------------------------
# PREMIUM TOOLS
# -------------------------------------------------

elif page == "Premium Tools":

    st.header("Premium Institutional Tools")

    st.warning("Upgrade required to access advanced analytics.")

    st.write("🔒 Institutional Flow Tracking")
    st.write("🔒 Hedge Fund Signals")
    st.write("🔒 AI Trading Predictions")
    st.write("🔒 Quant Risk Analysis")

    if st.button("Upgrade to Pro"):

        st.success("Redirecting to subscription system...")
