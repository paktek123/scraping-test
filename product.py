import requests
import humanize
import re
from bs4 import BeautifulSoup

class Product():
  def __init__(self, url):
    self.url = url

  def get_info(self):
    response = requests.get(self.url)
    if response.ok:
      soup = BeautifulSoup(response.content, 'html.parser')
      product_summary_div = soup.find('div', attrs={'class': 'productSummary'})
      title = product_summary_div.h1.text
      size_of_page = humanize.naturalsize(response.headers['content-length'])
      per_unit_price = float(re.sub(r'[^0-9.]', '', product_summary_div.findAll('p', 'pricePerUnit')[0].text.strip().split('/')[0]))
      description = soup.find('div', attrs={'class': 'productText'}).text.strip()
      return {"title": title, "size": size_of_page, "unit_price": per_unit_price, "description": description}
    else:
      return "Sorry couldn't retrieve the page."
