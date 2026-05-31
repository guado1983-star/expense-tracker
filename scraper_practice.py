import csv  # <-- 1. New built-in tool to handle Excel files
import requests
from bs4 import BeautifulSoup

url = "http://toscrape.com"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
scraped_products = []
book_containers = soup.find_all("article", class_="product_pod")

for book in book_containers:
    title = book.h3.a["title"]
    price_text = book.find("p", class_="price_color").text
    price = float(price_text.replace("£", ""))
    stock_text = book.find("p", class_="instock availability").text.strip()
    
    if stock_text == "In stock":
        stock_count = 10
    else:
        stock_count = 0

    product_dictionary = {
        "name": title,
        "price": price,
        "stock": stock_count
    }
    scraped_products.append(product_dictionary)

# --- 2. NEW CODE: SAVE TO EXCEL CSV FILE ---

# Define the file name we want to create
filename = "scraped_books.csv"

# Define the column headers for Excel
headers = ["name", "price", "stock"]