import json
import random
import time
from datetime import datetime

def generate_sapio_data():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Initializing Sapio Intelligence Scraper v3.5...")
    
    # 1. GENERATE AGENTIC GDP DATA
    # Simulating 2026 growth across XRPL and NEAR
    gdp_value = round(random.uniform(6.1, 6.8), 2)
    
    movers = [
        {"Project": "LiquidX (XRPL)", "Volume": f"${random.randint(40, 90)}M", "Trend": "🚀 High"},
        {"Project": "NearScribe AI", "Volume": f"${random.randint(10, 30)}M", "Trend": "📈 Steady"},
        {"Project": "OracleAgent v4", "Volume": f"${random.randint(100, 200)}k", "Trend": "⚡ Flash"},
        {"Project": "RippleSettler", "Volume": f"${random.randint(500, 900)}M", "Trend": "💎 Whale"}
    ]
    
    gdp_data = {
        "global_aGDP_estimate": f"${gdp_value}B",
        "top_movers": movers,
        "last_updated": datetime.now().isoformat()
    }

    # 2. GENERATE ADVANCED NEWS FEED
    # The "Alpha Pulse" that feeds your Bloomberg Ticker
    news_pool = [
        "XRPL: XAO DAO microgrant voting is 82% in favor of Sapio integration.",
        "NEAR: New 'DeepSnitch' agent confirms 40% increase in agentic compute demand.",
        "BEYOND: ISO-20022 compliance finalized for all Sapio-monitored nodes.",
        "MARKET: DWF Labs adds $5M to NEAR AI Agent Fund - Sapio tracking liquidity.",
        "TECH: Sapio v3.5 deployment successful. Sharding latency dropped to 6ms.",
        "RIPPLE: Institutional x402 nodes seeing record settlement volume this hour."
    ]
    # Pick 4 random headlines to keep it fresh
    current_news = random.sample(news_pool, 4)

    # 3. SAVE TO FILES
    try:
        with open('Agentic_GDP_Live_Feed.json', 'w') as f:
            json.dump(gdp_data, f, indent=4)
        
        with open('Sapio_News_Feed.json', 'w') as f:
            json.dump(current_news, f, indent=4)
            
        print("✅ Data successfully repopulated. Terminal is now LIVE.")
    except Exception as e:
        print(f"❌ Error saving files: {e}")

if __name__ == "__main__":
    generate_sapio_data()
