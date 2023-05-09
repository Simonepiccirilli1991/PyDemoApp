import requests
from bs4 import BeautifulSoup

url = "https://www.lego.com/it-it/themes/avatar"  # Replace with the URL of the website you want to scrape
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

# Find the paragraph using its unique identifier
soup = BeautifulSoup(html_content, "html.parser")

# Find all paragraphs within the HTML content
paragraphs = soup.select_one("div > div.ProductListingsstyles__PlpLayout-sc-1taio5c-1.ea-DaKE > div")

for paragraph in paragraphs:
    items = paragraph.find_all("li")  # Extract all <li> elements within the current paragraph

    for item in items:
        item_text = item.get_text()  # Extract the text content of each item
        words_to_replace = ["trovare", "desideri", "rating", "starsPrice"]

        modified_text = item_text

        for word in words_to_replace:
            modified_text = modified_text.replace(word, word + " ")

        print(modified_text)

    if not items:
        print("No items found in this paragraph.")