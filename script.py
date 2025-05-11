import requests
from bs4 import BeautifulSoup

def scrape_olx_car_covers():
    url = "https://www.olx.in/items/q-car-cover"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve OLX page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    listings = soup.find_all("a", href=True)

    with open("olx_car_covers.txt", "w", encoding="utf-8") as file:
        count = 0
        for link in listings:
            title = link.get_text(strip=True)
            href = link["href"]
            if "/item/" in href and title:
                file.write(f"{title}\nhttps://www.olx.in{href}\n\n")
                count += 1

    print(f"Scraped {count} car cover listings. Results saved to olx_car_covers.txt")

if __name__ == "__main__":
    scrape_olx_car_covers()
