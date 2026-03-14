import streamlit as st
import sqlite3
import pandas as pd
import requests
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Sapio Terminal",
    layout="wide",
    page_icon="⚡"
)

# -----------------------------
# CUSTOM STYLING
# -----------------------------

st.markdown("""
<style>
body {background-color:#0b0f19;}

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

.sidebar .sidebar-content {
    background:#020617;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# DATABASE
# -----------------------------

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

# -----------------------------
# MARKET DATA
# -----------------------------

def get_crypto_price(symbol):

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_24hr_vol=true&include_24hr_change=true"

    try:
        r = requests.get(url).json()

        data = r[symbol]

        return {
            "price": data["usd"],
            "volume": data["usd_24h_vol"],
            "change": data["usd_24h_change"]
        }

    except:
        return {"price":0,"volume":0,"change":0}

# -----------------------------
# AI SCORING
# -----------------------------

def ai_score(text):

    score = min(len(text) / 8, 100)

    return round(score,2)

# -----------------------------
# DATA LOADERS
# -----------------------------

def load_grants():

    return pd.read_sql_query("SELECT * FROM grants", conn)


def load_apps():

    return pd.read_sql_query("SELECT * FROM applications", conn)

# -----------------------------
# SIDEBAR NAV
# -----------------------------

st.sidebar.title("⚡ SAPIO TERMINAL")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Create Grant",
        "Marketplace",
        "Apply",
        "Review"
    ]
)

# -----------------------------
# DASHBOARD
# -----------------------------

if page == "Dashboard":

    st.title("⚡ Sapio Grant Infrastructure")

    btc = get_crypto_price("bitcoin")
    eth = get_crypto_price("ethereum")
    sol = get_crypto_price("solana")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("BTC Price", f"${btc['price']}", f"{btc['change']:.2f}%")
        st.caption(f"24h Vol: ${btc['volume']:.0f}")

    with col2:
        st.metric("ETH Price", f"${eth['price']}", f"{eth['change']:.2f}%")
        st.caption(f"24h Vol: ${eth['volume']:.0f}")

    with col3:
        st.metric("SOL Price", f"${sol['price']}", f"{sol['change']:.2f}%")
        st.caption(f"24h Vol: ${sol['volume']:.0f}")

    st.divider()

    grants = load_grants()
    apps = load_apps()

    c1,c2,c3 = st.columns(3)

    c1.metric("Total Grants", len(grants))
    c2.metric("Applications", len(apps))
    c3.metric("Approved", len(apps[apps.status == "approved"]))

    st.divider()

    st.subheader("Grant Activity")

    if len(grants)>0:
        st.dataframe(grants)

# -----------------------------
# CREATE GRANT
# -----------------------------

if page == "Create Grant":

    st.header("Create Grant Program")

    title = st.text_input("Grant Title")

    ecosystem = st.selectbox(
        "Ecosystem",
        ["Ethereum","Solana","XRP","AI","Research"]
    )

    budget = st.number_input("Budget")

    description = st.text_area("Description")

    if st.button("Create Grant"):

        c.execute(
            "INSERT INTO grants VALUES(NULL,?,?,?,?,?)",
            (title,ecosystem,budget,description,datetime.now())
        )

        conn.commit()

        st.success("Grant created")

# -----------------------------
# MARKETPLACE
# -----------------------------

if page == "Marketplace":

    st.header("Grant Marketplace")

    grants = load_grants()

    for _,row in grants.iterrows():

        with st.container():

            st.markdown("### " + row['title'])
            st.write("Ecosystem:",row['ecosystem'])
            st.write("Budget:",row['budget'])
            st.write(row['description'])

            st.divider()

# -----------------------------
# APPLY
# -----------------------------

if page == "Apply":

    st.header("Apply for Grant")

    grants = load_grants()

    if len(grants)==0:

        st.info("No grants available")

    else:

        titles = grants['title'].tolist()

        selected = st.selectbox("Grant",titles)

        name = st.text_input("Applicant Name")

        github = st.text_input("Github Repo")

        proposal = st.text_area("Proposal")

        if st.button("Submit"):

            gid = int(grants[grants.title==selected].id.values[0])

            score = ai_score(proposal)

            c.execute(
                "INSERT INTO applications VALUES(NULL,?,?,?,?,?,?)",
                (gid,name,github,proposal,score,"submitted")
            )

            conn.commit()

            st.success(f"Application submitted | AI Score: {score}")

# -----------------------------
# REVIEW
# -----------------------------

if page == "Review":

    st.header("Grant Review Console")

    apps = load_apps()

    if len(apps)==0:

        st.info("No applications")

    for _,row in apps.iterrows():

        st.subheader(row['applicant'])
        st.write("Github:",row['github'])
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
