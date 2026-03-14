import streamlit as st
import pandas as pd
import random
import time
import requests
from datetime import datetime

# --- 1. PROTOCOL ARCHITECTURE & CSS ---
st.set_page_config(page_title="Sapio Intelligence Terminal", page_icon="⚙️", layout="wide")

st.markdown("""
    <style>
    /* Global Terminal Theme */
    .stApp { background-color: #0b0e11; color: #d1d4dc; }
    
    /* Dexscreener-Style Borders */
    div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background: #131722;
        border: 1px solid #363a45;
        border-radius: 4px;
        padding: 15px;
        margin-bottom: 5px;
    }
    
    /* Code/Terminal Text */
    .stCodeBlock { border: 1px solid #2962ff !important; border-radius: 2px !important; }
    
    /* Professional Metrics */
    [data-testid="stMetricValue"] { color: #22ab94 !important; font-family: 'JetBrains Mono', monospace; font-size: 1.4rem !important; }
    
    /* Custom Scrollbar for the 'Pro' feel */
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-thumb { background: #363a45; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE RUST/SOLIDITY ENGINE ---
def get_protocol_code(lang):
    if lang == "Rust":
        return """#[near_bindgen]
pub fn solve_intent(intent: String, min_return: u128) -> Promise {
    let sapio_guard = env::predecessor_account_id();
    log!("Protocol Secured: {}", sapio_guard);
    ext_dex::swap(intent).then(Self::settle_fee())
}"""
    return """contract SapioTerminal {
    event IntentSettled(address indexed user, uint256 fee);
    function execute(bytes32 _id) external payable {
        require(msg.value > 0.001 ether);
        (bool s,) = treasury.call{value: msg.value}("");
        emit IntentSettled(msg.sender, msg.value);
    }
}"""

# --- 3. DATA & ANALYTICS ---
@st.cache_resource
def init_treasury():
    return {"rev": 1240.50, "m": 412, "vol": 14820930}

def fetch_market():
    try: return requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ripple,near,bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true").json()
    except: return None

store = init_treasury()
mkt = fetch_market()

# --- 4. NAVIGATION STRIP (CoinMarketCap Style) ---
ticker_cols = st.columns(6)
symbols = [("BTC", "bitcoin"), ("ETH", "ethereum"), ("XRP", "ripple"), ("NEAR", "near"), ("SOL", "solana")]
for i, (sym, cid) in enumerate(symbols):
    if mkt:
        price = mkt[cid]['usd']
        change = mkt[cid]['usd_24h_change']
        ticker_cols[i].metric(sym, f"${price}", f"{round(change, 2)}%")
ticker_cols[5].metric("SYSTEM", "STABLE", "14ms")

st.divider()

# --- 5. THE TRIPLE-PANE TERMINAL (GMGN Style) ---
# Left: Stats | Center: Command & Charts | Right: Protocol Code
L, C, R = st.columns([1, 2.2, 1.3])

with L:
    st.markdown("#### 🏦 SAPIO TREASURY")
    st.metric("Total Revenue", f"${round(store['rev'], 2)}", "Active Fee Flow")
    st.metric("Total Volume", f"${store['vol']:,}")
    
    st.divider()
    st.markdown("#### 🔐 AUTHENTICATION")
    if 'auth' not in st.session_state: st.session_state.auth = False
    if not st.session_state.auth:
        if st.button("CONNECT PROTOCOL ID"):
            st.session_state.auth = True
            st.rerun()
    else:
        st.success(f"ID: r{random.randint(100,999)}...SAPIO")
        if st.button("TERMINATE SESSION"):
            st.session_state.auth = False
            st.rerun()

with C:
    st.markdown("#### ⚡ INTENT EXECUTION (MAINNET)")
    with st.container():
        intent = st.text_input("Define Autonomous Mission", placeholder="e.g. Liquidate undercollateralized NEAR pools", disabled=not st.session_state.auth)
        if st.button("EXECUTE ON CLOUD", disabled=not st.session_state.auth):
            with st.status("Solving via Rust-WASM Kernel..."):
                time.sleep(1.2)
                fee = round(random.uniform(0.15, 0.95), 2)
                store['rev'] += fee
                store['m'] += 1
            st.success(f"Mission Signed. Fee Collected: ${fee}")
    
    # Live Chart Simulation (Dexscreener Style)
    st.markdown("#### 💹 REVENUE MOMENTUM")
    chart_data = pd.DataFrame(random.sample(range(1000, 1300), 15), columns=['Revenue'])
    st.area_chart(chart_data, color="#2962ff", height=200)

with R:
    st.markdown("#### ⚙️ CORE PROTOCOL")
    st.tabs(["Rust (Near)", "Solidity (EVM)"])
    st.caption("Immutable Smart Contract Source")
    st.code(get_protocol_code("Rust"), language="rust")
    st.code(get_protocol_code("Solidity"), language="solidity")
    
    st.divider()
    st.markdown("#### 📡 LIVE ORDER FLOW")
    for _ in range(3):
        st.caption(f"[{datetime.now().strftime('%H:%M:%S')}] INTENT_SIGNED: {random.randint(100,999)} XRP")

# --- 6. FOOTER ---
st.markdown("---")
st.caption(f"SAPIO INTELLIGENCE • v12.0.1 • PRODUCTION READY • CLOUD NODES: {random.randint(8,12)} ACTIVE")
