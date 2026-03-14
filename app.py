import streamlit as st
import sqlite3
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

# ======================================================
# SAPIO TERMINAL - FULL MVP BUILD
# Grant Infrastructure + Grant Intelligence + AI Console
# ======================================================

st.set_page_config(page_title="Sapio Terminal", layout="wide", page_icon="⚡")

# ======================================================
# STYLING
# ======================================================

st.markdown("""
<style>
body {background-color:#0b0f19}
.block-container {padding-top:1rem}

.metric-card {
    background: linear-gradient(145deg,#111827,#0b1220);
    padding:20px;
    border-radius:12px;
    border:1px solid #1f2937;
}

.market-card {
    background:#0f172a;
    padding:15px;
    border-radius:10px;
    border:1px solid #1e293b;
}

textarea, input {
    background-color:#020617 !important;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# DATABASE
# ======================================================

conn = sqlite3.connect("sapio.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS grants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    ecosystem TEXT,
    budget REAL,
    description TEXT,
    created_at TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grant_id INTEGER,
    applicant TEXT,
    github TEXT,
    proposal TEXT,
    score REAL,
    status TEXT
)
""")

conn.commit()

# ======================================================
# MARKET DATA
# ======================================================

def get_crypto(symbol):

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true"

    try:
        r = requests.get(url).json()
        d = r[symbol]

        return {
            "price": d["usd"],
            "change": d["usd_24h_change"],
            "volume": d["usd_24h_vol"]
        }

    except:
        return {"price":0,"change":0,"volume":0}


# ======================================================
# AI PROPOSAL SCORING
# ======================================================

def ai_score(text):

    words = len(text.split())
    score = min(words * 0.5, 100)

    return round(score,2)


# ======================================================
# GRANT INTELLIGENCE ENGINE
# ======================================================

def grant_intelligence():

    grants = pd.read_sql_query("SELECT * FROM grants", conn)
    apps = pd.read_sql_query("SELECT * FROM applications", conn)

    if len(grants) == 0:
        st.info("No data yet")
        return

    st.subheader("Grant Distribution")

    fig = px.pie(grants, names="ecosystem", title="Grants by Ecosystem")

    st.plotly_chart(fig, use_container_width=True)

    if len(apps) > 0:

        st.subheader("Application Scores")

        fig2 = px.histogram(apps, x="score", nbins=20)

        st.plotly_chart(fig2, use_container_width=True)


# ======================================================
# AI COMMAND CONSOLE
# ======================================================

def ai_console():

    st.subheader("⚡ AI Command Console")

    cmd = st.text_input("Enter command", placeholder="analyze grant ecosystem")

    if st.button("Execute"):

        if "analyze" in cmd:

            grants = pd.read_sql_query("SELECT * FROM grants", conn)

            if len(grants)==0:
                st.write("No grants to analyze")
                return

            ecosystem_counts = grants['ecosystem'].value_counts()

            st.write("Top ecosystems:")
            st.write(ecosystem_counts)

        elif "market" in cmd:

            btc = get_crypto("bitcoin")

            st.write("BTC Market Data")
            st.json(btc)

        else:

            st.write("Command not recognized")


# ======================================================
# LOADERS
# ======================================================

def load_grants():

    return pd.read_sql_query("SELECT * FROM grants", conn)


def load_apps():

    return pd.read_sql_query("SELECT * FROM applications", conn)


# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("⚡ SAPIO TERMINAL")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Grant Marketplace",
        "Create Grant",
        "Apply",
        "Review",
        "Grant Intelligence",
        "AI Command Console"
    ]
)


# ======================================================
# DASHBOARD
# ======================================================

if page == "Dashboard":

    st.title("Sapio Sovereign Grant Terminal")

    btc = get_crypto("bitcoin")
    eth = get_crypto("ethereum")
    sol = get_crypto("solana")

    col1,col2,col3 = st.columns(3)

    col1.metric("BTC", f"${btc['price']}", f"{btc['change']:.2f}%")
    col1.caption(f"Volume ${btc['volume']:.0f}")

    col2.metric("ETH", f"${eth['price']}", f"{eth['change']:.2f}%")
    col2.caption(f"Volume ${eth['volume']:.0f}")

    col3.metric("SOL", f"${sol['price']}", f"{sol['change']:.2f}%")
    col3.caption(f"Volume ${sol['volume']:.0f}")

    st.divider()

    grants = load_grants()
    apps = load_apps()

    c1,c2,c3 = st.columns(3)

    c1.metric("Total Grants", len(grants))

    c2.metric("Applications", len(apps))

    c3.metric("Approved", len(apps[apps.status == "approved"]))


# ======================================================
# CREATE GRANT
# ======================================================

if page == "Create Grant":

    st.header("Create Grant Program")

    title = st.text_input("Grant Title")

    ecosystem = st.selectbox(
        "Ecosystem",
        ["Ethereum","Solana","XRP","AI","Research"]
    )

    budget = st.number_input("Budget", min_value=0.0)

    description = st.text_area("Description")

    if st.button("Create Grant"):

        c.execute(
            "INSERT INTO grants VALUES(NULL,?,?,?,?,?)",
            (title,ecosystem,budget,description,datetime.now())
        )

        conn.commit()

        st.success("Grant created")


# ======================================================
# MARKETPLACE
# ======================================================

if page == "Grant Marketplace":

    st.header("Active Grants")

    grants = load_grants()

    if len(grants)==0:
        st.info("No grants available")

    for _,row in grants.iterrows():

        st.subheader(row['title'])
        st.write("Ecosystem:",row['ecosystem'])
        st.write("Budget:",row['budget'])
        st.write(row['description'])

        st.divider()


# ======================================================
# APPLY
# ======================================================

if page == "Apply":

    st.header("Apply For Grant")

    grants = load_grants()

    if len(grants)==0:
        st.info("No grants available")

    else:

        titles = grants['title'].tolist()

        selected = st.selectbox("Select Grant",titles)

        name = st.text_input("Applicant Name")

        github = st.text_input("GitHub Repo")

        proposal = st.text_area("Proposal")

        if st.button("Submit Application"):

            gid = int(grants[grants.title==selected].id.values[0])

            score = ai_score(proposal)

            c.execute(
                "INSERT INTO applications VALUES(NULL,?,?,?,?,?,?)",
                (gid,name,github,proposal,score,"submitted")
            )

            conn.commit()

            st.success(f"Submitted | AI Score: {score}")


# ======================================================
# REVIEW
# ======================================================

if page == "Review":

    st.header("Grant Review Console")

    apps = load_apps()

    if len(apps)==0:
        st.info("No applications")

    for _,row in apps.iterrows():

        st.subheader(row['applicant'])
        st.write("GitHub:",row['github'])
        st.write("Score:",row['score'])
        st.write("Status:",row['status'])

        col1,col2 = st.columns(2)

        if col1.button(f"Approve {row['id']}"):

            c.execute(
                "UPDATE applications SET status='approved' WHERE id=?",
                (row['id'],)
            )

            conn.commit()

            st.rerun()

        if col2.button(f"Reject {row['id']}"):

            c.execute(
                "UPDATE applications SET status='rejected' WHERE id=?",
                (row['id'],)
            )

            conn.commit()

            st.rerun()

        st.divider()


# ======================================================
# GRANT INTELLIGENCE PAGE
# ======================================================

if page == "Grant Intelligence":

    st.header("Grant Intelligence Engine")

    grant_intelligence()


# ======================================================
# AI COMMAND CONSOLE PAGE
# ======================================================

if page == "AI Command Console":

    ai_console()

