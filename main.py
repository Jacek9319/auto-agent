import requests
from bs4 import BeautifulSoup
import datetime

keywords = ["ford fiesta", "hyundai i30"]
base_url = "https://www.kleinanzeigen.de/s-autos/c216"
today = datetime.datetime.now().strftime("%Y-%m-%d")

def search(keyword):
    print(f"\n🔎 Szukam: {keyword.upper()}")
    params = {
        "ad": "offer",
        "q": keyword,
        "min-auto_year": "2009",
        "max-auto_year": "2013",
        "priceTo": "2200",
        "sortingField": "PRICE",
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("❌ Błąd pobierania strony")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select("article.aditem")

    for ad in results[:5]:
        title = ad.select_one(".ellipsis").text.strip() if ad.select_one(".ellipsis") else "Brak tytułu"
        price = ad.select_one(".aditem-main--middle--price-shipping--price").text.strip() if ad.select_one(".aditem-main--middle--price-shipping--price") else "Brak ceny"
        link = "https://www.kleinanzeigen.de" + ad.a["href"]
        print(f"📌 {title} – {price}\n🔗 {link}\n")

if __name__ == "__main__":
    print(f"🚀 Start agenta – {today}")
    for word in keywords:
        search(word)
