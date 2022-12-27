import requests
import json
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get("SOME_WHERE")

soup = BeautifulSoup(response.text, 'lxml')

# Find the element containing the list of products
product_list = soup.select_one(".product-cards-list div.row:first-child")

# Extract the individual products from the list
products = product_list.select(".product-card-item")

print(products)
# Create a list to store the data
data = []


for product in products:
    title_element = product.select_one(".title a")
    id_element = product.select_one(".title h3")
    
    print(id_element["data-id"])
    print(title_element["href"])
    
    print(product)
    
    # Add the data for the product to the list
    data.append({"title": title_element["href"], "id": id_element["data-id"]})


# Save the data to a JSON file
with open("products.json", "w") as outfile:
    json.dump(data, outfile)
    
# with open('/var/www/py-scrape/src/home.html', 'r') as html_file:
    # content = html_file.read()

    

    # print(soup.prettify())

