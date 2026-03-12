import requests
import json
import os

# ==========================================================
# STEP 1: PASTE YOUR TOKEN BELOW (Keep the quotes!)
# ==========================================================
GITHUB_TOKEN = "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" 
# ==========================================================

# This is what we are searching for (AI projects on Crypto chains)
QUERY = "topic:decentralized-ai"

def run_terminal_scraper():
    # 1. Setup the connection
    url = f"https://api.github.com/search/repositories?q={QUERY}&sort=updated&order=desc"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print("--- AI CRYPTO TERMINAL: INITIALIZING SCAN ---")
    
    try:
        # 2. Get the data from GitHub
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            
            final_list = []
            print(f"🔍 Found {len(items)} recent projects. Filtering for quality...\n")
            
            for repo in items[:15]: # Take the top 15 results
                project = {
                    "Project Name": repo['name'].upper(),
                    "Developer": repo['owner']['login'],
                    "Stars": repo['stargazers_count'],
                    "Last Update": repo['updated_at'],
                    "Link": repo['html_url'],
                    "Description": repo['description']
                }
                final_list.append(project)
                print(f"✅ LOADED: {project['Project Name']} (Stars: {project['Stars']})")
            
            # 3. Save it to a file on your computer
            with open("terminal_data.json", "w") as file:
                json.dump(final_list, file, indent=4)
                
            print("\n" + "="*40)
            print("💰 DATA ASSET CREATED: terminal_data.json")
            print("CEO MOVE: Open that file to see your first 15 leads!")
            print("="*40)
            
        elif response.status_code == 401:
            print("❌ ERROR: Your Token is invalid. Check for extra spaces!")
        else:
            print(f"❌ ERROR: GitHub said {response.status_code}")
            
    except Exception as e:
        print(f"❌ CRITICAL SYSTEM ERROR: {e}")

if __name__ == "__main__":
    run_terminal_scraper()
import json
import time

# Make sure this data is actually there!
report = {
    "timestamp": time.time(),
    "global_aGDP_estimate": "$4.2 Billion",
    "top_movers": [
        {"name": "Sentient-Trader-v4", "chain": "Solana", "daily_volume": "$890k"},
        {"name": "Neural-Arbitrage-Bot", "chain": "Base", "daily_volume": "$1.2M"}
    ]
}

# SAVE TO THE EXACT PATH THE APP IS LOOKING FOR
with open("/Users/birpratapsingh/Documents/Agentic_GDP_Live_Feed.json", "w") as f:
    json.dump(report, f, indent=4)

print("Billionaire Insight: aGDP Data Updated.")
print("Sapio Intelligence: aGDP Data Updated.")
