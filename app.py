import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import numpy as np

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="Sapio Finance Terminal",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# PROFESSIONAL CSS
# -------------------------------

st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main-title {
    font-size:40px;
    font-weight:700;
}
.metric-box {
    background-color:#1c1f26;
    padding:15px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------

st.markdown("<p class='main-title'>📊 Sapio Finance Terminal</p>", unsafe_allow_html=True)
st.write("AI Powered Market Intelligence Platform")

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------

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
        "Premium Tools"
    ]
)

# -------------------------------
# MARKET DASHBOARD
# -------------------------------

if page == "Market Dashboard":

    st.header("Global Market Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("S&P 500", "5,120", "+1.2%")
    col2.metric("NASDAQ", "16,320", "+0.8%")
    col3.metric("Bitcoin", "$68,200", "+2.4%")
    col4.metric("Gold", "$2,150", "+0.5%")

    st.subheader("Market Trends")

    data = px.data.stocks()

    fig = px.line(
        data,
        x="date",
        y=data.columns[1:],
        title="Global Market Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# STOCK ANALYZER
# -------------------------------

elif page == "Stock Analyzer":

    st.header("Stock Analysis Tool")

    ticker = st.text_input("Enter Stock Ticker", "AAPL")

    period = st.selectbox(
        "Select Period",
        ["1mo","3mo","6mo","1y","5y"]
    )

    if st.button("Analyze Stock"):

        stock = yf.download(ticker, period=period)

        fig = px.line(
            stock,
            x=stock.index,
            y="Close",
            title=f"{ticker} Price Chart"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Raw Data")

        st.dataframe(stock.tail(20))

# -------------------------------
# CRYPTO DASHBOARD
# -------------------------------

elif page == "Crypto Dashboard":

    st.header("Crypto Market Dashboard")

    crypto_data = {
        "Coin": ["Bitcoin","Ethereum","Solana","BNB"],
        "Price":[68200,3500,145,410],
        "Change":[2.4,1.8,3.5,1.1]
    }

    df = pd.DataFrame(crypto_data)

    st.dataframe(df)

    fig = px.bar(
        df,
        x="Coin",
        y="Price",
        title="Crypto Prices"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# AI INSIGHTS
# -------------------------------

elif page == "AI Market Insights":

    st.header("AI Market Insights")

    st.write(
        "AI generated analysis of current market trends."
    )

    if st.button("Generate Insight"):

        insights = [
            "Technology stocks showing strong upward momentum.",
            "Crypto market entering bullish accumulation phase.",
            "Energy sector outperforming global markets.",
            "AI companies attracting institutional capital."
        ]

        st.success(np.random.choice(insights))

# -------------------------------
# SENTIMENT ANALYSIS
# -------------------------------

elif page == "Sentiment Analysis":

    st.header("Market Sentiment")

    sentiment_data = {
        "Sector":[
            "Technology",
            "Energy",
            "Finance",
            "Healthcare"
        ],
        "Sentiment":[
            0.78,
            0.62,
            0.55,
            0.48
        ]
    }

    df = pd.DataFrame(sentiment_data)

    fig = px.bar(
        df,
        x="Sector",
        y="Sentiment",
        title="Market Sentiment Score"
    )

    st.plotly_chart(fig)

# -------------------------------
# PORTFOLIO TRACKER
# -------------------------------

elif page == "Portfolio Tracker":

    st.header("Investment Portfolio")

    ticker = st.text_input("Ticker")

    amount = st.number_input("Investment Amount")

    if st.button("Add Investment"):

        st.success(f"Added {ticker} investment worth ${amount}")

# -------------------------------
# PREMIUM TOOLS
# -------------------------------

elif page == "Premium Tools":

    st.header("Premium Investor Tools")

    st.warning("Upgrade to unlock premium analytics.")

    st.write("🔒 Hedge Fund Signals")
    st.write("🔒 Institutional Flow Data")
    st.write("🔒 AI Trading Signals")
    st.write("🔒 Quantitative Risk Analysis")

    if st.button("Upgrade to Pro"):

        st.success("Redirecting to subscription system...")
