import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.olx.in/items/q-car-cover"

# Send HTTP GET request
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# Check response status
if response.status_code != 200:
    print(f"Failed to retrieve OLX page. Status code: {response.status_code}")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# File to write the results
output_file = "olx_car_covers.txt"
with open(output_file, "w", encoding="utf-8") as file:
    listings = soup.find_all("a", href=True)
    count = 0

    for link in listings:
        title = link.get_text(strip=True)
        href = link["href"]
        if "/item/" in href and title:
            file.write(f"{title}\nhttps://www.olx.in{href}\n\n")
            count += 1

print(f"Scraped {count} car cover listings. Results saved to {output_file}")
