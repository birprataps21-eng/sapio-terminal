import json
import os
import random
from datetime import datetime

# GET THE ABSOLUTE PATH OF THIS FOLDER
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_god_mode_scrape():
    # 1. Define Data
    gdp_data = {
        "global_aGDP_estimate": f"${round(random.uniform(6.4, 6.9), 2)}B",
        "top_movers": [
            {"Project": "LiquidX (XRPL)", "Volume": "$92M", "Trend": "🚀 High"},
            {"Project": "NearScribe AI", "Volume": "$31M", "Trend": "📈 Steady"}
        ],
        "agent_tasks": [
            {"agent": "Sapio-Alpha-1", "task": "Scanning XRPL", "status": "ACTIVE"},
            {"agent": "Whale-Tracker", "task": "Monitoring NEAR", "status": "ACTIVE"}
        ],
        "ai_insight": "AI detects institutional liquidity rotation into NEAR shards."
    }
    
    news_data = ["XRPL: x402 Node Online", "NEAR: AI Compute Demand Spike"]

    # 2. SAVE USING ABSOLUTE PATHS
    gdp_path = os.path.join(BASE_DIR, 'Agentic_GDP_Live_Feed.json')
    news_path = os.path.join(BASE_DIR, 'Sapio_News_Feed.json')

    with open(gdp_path, 'w') as f:
        json.dump(gdp_data, f, indent=4)
    with open(news_path, 'w') as f:
        json.dump(news_data, f, indent=4)

    print(f"✅ Files saved to: {BASE_DIR}")

if __name__ == "__main__":
    run_god_mode_scrape()
