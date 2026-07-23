import requests
from bs4 import BeautifulSoup
import csv

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Each product is inside a div with class "product-wrapper"
    products = soup.select("div.product-wrapper")

    scraped_data = []

    for product in products:
        title = product.select_one("a.title").text.strip()
        price = product.select_one("h4.price").text.strip()

        # Star rating is stored as the number of "ratings" divs with filled stars
        rating_div = product.select_one("div.ratings")
        rating = len(rating_div.select("span.ws-icon-star")) if rating_div else "N/A"

        reviews = product.select_one("p.review-count").text.strip()

        scraped_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Reviews": reviews
        })

    # Print results
    for item in scraped_data:
        print(item)

    # Save to CSV
    with open("laptops.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Price", "Rating", "Reviews"])
        writer.writeheader()
        writer.writerows(scraped_data)

    print(f"\nSaved {len(scraped_data)} products to laptops.csv")

else:
    print(f"Failed to fetch page: {response.status_code}")
