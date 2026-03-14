import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.grants.gov/search-results.html"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

grants = []

for item in soup.find_all("div",class_="search-result-item"):

    title = item.find("a").text.strip()

    grants.append({
        "Grant":title,
        "Funding":"Unknown",
        "Category":"General",
        "Region":"US",
        "Deadline":"Unknown"
    })

df = pd.DataFrame(grants)

df.to_csv("grants.csv",index=False)

print("Grant database created!")
