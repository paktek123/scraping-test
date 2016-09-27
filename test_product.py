from product import Product

class TestProduct:

    def setup(self):
        self.product = Product('http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-apricot-ripe---ready-320g.html')

    def teardown(self):
        pass

    def test_get_info(self):
        """
        Check if the data is valid when returned
        """
        result = self.product.get_info()
        assert type(result) == dict

    def test_product_summary_has_title_key(self):
        """
        Should return results key
        """
        result = self.product.get_info()
        assert ('title' in result) == True

    def test_product_summary_has_size_key(self):
        """
        Should return results key
        """
        result = self.product.get_info()
        assert ('size' in result) == True

    def test_product_summary_has_unit_price_key(self):
        """
        Should return results key
        """
        result = self.product.get_info()
        assert ('unit_price' in result) == True

    def test_product_summary_has_description_key(self):
        """
        Should return results key
        """
        result = self.product.get_info()
        assert ('description' in result) == True
