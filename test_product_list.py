from product_list import ProductList
from nose.tools import *
import requests
import json

class TestProductList:

    def setup(self):
        self.product_list = ProductList('http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html')
        self.bogus_product_list = ProductList('http://doesnotexistandisfake.co.uk')
        self.product_list.generate_soup()

    def teardown(self):
        pass

    def test_generate_soup(self):
        """
        Check if soup is generated for successful link
        """
        assert hasattr(self.product_list, 'soup') == True

    @raises(requests.exceptions.ConnectionError)
    def test_bogus_soup(self):
        """
        There should be no soup if request failed
        """
        self.bogus_product_list.generate_soup()

    def test_should_return_a_list(self):
        """
        Return a list
        """
        result = self.product_list.get_product_urls()
        assert type(result) == list

    def test_to_json_valid_json(self):
        """
        Should return valid JSON
        """
        result = json.loads(self.product_list.to_json())
        assert type(result) == dict

    def test_to_json_has_results_key(self):
        """
        Should return results key
        """
        result = json.loads(self.product_list.to_json())
        assert ('results' in result) == True

    def test_to_json_has_total_key(self):
        """
        Should return results key
        """
        result = json.loads(self.product_list.to_json())
        assert ('total' in result) == True
