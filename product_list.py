import requests
import json
from bs4 import BeautifulSoup
from product import Product

class ProductList():
  def __init__(self, url):
    self.url = url
    self.total_prices = []

  def generate_soup(self):
    response = requests.get(self.url, timeout=2)
    if response.ok:
      self.soup = BeautifulSoup(response.content, 'html.parser')
    else:
      return "Sorry couldn't retrieve the page."

  def get_product_urls(self):
    return [link.a.attrs['href'] for link in self.soup.findAll('div', attrs={'class':'product'})]

  def to_json(self):
    product_urls = self.get_product_urls()
    results = []
    total_price = 0

    for url in product_urls:
      product = Product(url)
      product_info = product.get_info()
      results.append(product_info)
      total_price += product_info['unit_price']

    return json.dumps({"results": results, "total": round(total_price,2)})
