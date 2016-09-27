#!/usr/bin/env python

from product_list import ProductList

product_list = ProductList('http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html')
product_list.generate_soup()
print(product_list.to_json())
