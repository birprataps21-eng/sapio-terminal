import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# -----------------------------
# Database Setup
# -----------------------------
conn = sqlite3.connect("sapio.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    wallet TEXT
)
""")

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
# Helper Functions
# -----------------------------

def ai_score_proposal(text):
    """Mock AI scoring system"""
    length = len(text)
    score = min(100, (length / 10))
    return round(score, 2)


def fetch_grants():
    return pd.read_sql_query("SELECT * FROM grants", conn)


def fetch_apps():
    return pd.read_sql_query("SELECT * FROM applications", conn)


# -----------------------------
# UI CONFIG
# -----------------------------

st.set_page_config(
    page_title="Sapio Grant Terminal",
    layout="wide",
)

st.title("⚡ Sapio Grant Infrastructure")

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Create Grant",
        "Grant Marketplace",
        "Apply For Grant",
        "Review Applications",
    ],
)

# -----------------------------
# DASHBOARD
# -----------------------------

if page == "Dashboard":

    grants = fetch_grants()
    apps = fetch_apps()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Grants", len(grants))
    col2.metric("Applications", len(apps))
    col3.metric("Approved", len(apps[apps.status == "approved"]))

    st.subheader("Recent Grants")
    st.dataframe(grants.tail(10))

    st.subheader("Application Activity")
    st.dataframe(apps.tail(10))


# -----------------------------
# CREATE GRANT
# -----------------------------

if page == "Create Grant":

    st.header("Create Grant Program")

    title = st.text_input("Grant Title")

    ecosystem = st.selectbox(
        "Ecosystem",
        ["Ethereum", "Solana", "XRP", "AI Research", "Other"],
    )

    budget = st.number_input("Grant Budget", min_value=0.0)

    description = st.text_area("Grant Description")

    if st.button("Create Grant"):

        c.execute(
            "INSERT INTO grants VALUES (NULL,?,?,?,?,?)",
            (title, ecosystem, budget, description, datetime.now()),
        )

        conn.commit()

        st.success("Grant Created")


# -----------------------------
# MARKETPLACE
# -----------------------------

if page == "Grant Marketplace":

    st.header("Active Grants")

    grants = fetch_grants()

    for _, row in grants.iterrows():

        with st.container():

            st.subheader(row["title"])
            st.write("Ecosystem:", row["ecosystem"])
            st.write("Budget:", row["budget"])
            st.write(row["description"])

            st.divider()


# -----------------------------
# APPLY
# -----------------------------

if page == "Apply For Grant":

    st.header("Submit Grant Application")

    grants = fetch_grants()

    grant_titles = grants["title"].tolist()

    selected = st.selectbox("Select Grant", grant_titles)

    applicant = st.text_input("Your Name")

    github = st.text_input("GitHub Repository")

    proposal = st.text_area("Proposal")

    if st.button("Submit Application"):

        grant_id = int(grants[grants.title == selected].id.values[0])

        score = ai_score_proposal(proposal)

        c.execute(
            "INSERT INTO applications VALUES (NULL,?,?,?,?,?,?)",
            (grant_id, applicant, github, proposal, score, "submitted"),
        )

        conn.commit()

        st.success(f"Application submitted. AI Score: {score}")


# -----------------------------
# REVIEW
# -----------------------------

if page == "Review Applications":

    st.header("Reviewer Console")

    apps = fetch_apps()

    if len(apps) == 0:
        st.info("No applications yet")

    for _, row in apps.iterrows():

        with st.container():

            st.subheader(row["applicant"])
            st.write("GitHub:", row["github"])
            st.write("Score:", row["score"])
            st.write("Status:", row["status"])

            col1, col2 = st.columns(2)

            if col1.button(f"Approve {row['id']}"):

                c.execute(
                    "UPDATE applications SET status='approved' WHERE id=?",
                    (row["id"],),
                )

                conn.commit()

                st.rerun()

            if col2.button(f"Reject {row['id']}"):

                c.execute(
                    "UPDATE applications SET status='rejected' WHERE id=?",
                    (row["id"],),
                )

                conn.commit()

                st.rerun()

            st.divider()
