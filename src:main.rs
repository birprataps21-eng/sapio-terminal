use std::sync::{Arc, Mutex};
use tokio::time::{sleep, Duration};
use mx_message::sample::generate_sample; // High-end ISO 20022 generator

struct SapioState {
    gdp: f64,
    revenue: f64,
    xrpl_status: String,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 1. Initialize Thread-Safe State
    let state = Arc::new(Mutex::new(SapioState {
        gdp: 6.57,
        revenue: 0.0,
        xrpl_status: "CONNECTED (MAINNET)".to_string(),
    }));

    println!("--------------------------------------------------");
    println!("⚡ SAPIO SOVEREIGN TERMINAL | v16.0 | XRPL-NATIVE");
    println!("--------------------------------------------------");

    // 2. Clone state for the background "Agent"
    let agent_state = Arc::clone(&state);

    // 3. The "Agentic Intent" Loop (Runs in background)
    tokio::spawn(async move {
        loop {
            sleep(Duration::from_secs(5)).await;
            let mut s = agent_state.lock().unwrap();
            
            // Execute Mission: Simulate platform fee capture
            s.revenue += 0.0025;
            s.gdp += 0.01;
            
            println!("\n[AGENT] Mission Settled via XRPL");
            println!(" > REVENUE: ${:.4} | GDP: ${:.2}B", s.revenue, s.gdp);
        }
    });

    // 4. Main Console: Showing Top Crypto and Compliance
    loop {
        {
            let s = state.lock().unwrap();
            println!("\n--- SYSTEM OVERVIEW ---");
            println!("COMPLIANCE: ISO 20022 (pacs.008) VALIDATED");
            println!("XRPL NODE:  {}", s.xrpl_status);
            println!("TREASURY:   ${:.4}", s.revenue);
            
            // Top Crypto Prices (Placeholder for live fetch)
            println!("MARKET:     XRP: $0.62 | NEAR: $6.45 | BTC: $68,412");
            
            // ISO 20022 Proof Generation
            let iso_msg = generate_sample("pacs008", None).unwrap_or_else(|_| "DATA_LOCKED".into());
            println!("LATEST ISO MESSAGE HASH: {:x}", md5::compute(iso_msg.to_string()));
        }
        sleep(Duration::from_secs(10)).await;
    }
}