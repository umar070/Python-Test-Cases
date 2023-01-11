from selenium import webdriver
import unittest

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_website_loads(self):
        self.driver.get("https://theviewoptique.com/")
        self.assertIn("TheViewOptique", self.driver.title)

    def test_website_loads2(self):
        self.driver.get("https://theviewoptique.com/Products.aspx?FrameShape=Round")
        self.assertIn("", self.driver.title)

    def test_website_WayFarer(self):
        self.driver.get("https://theviewoptique.com/Products.aspx?StyleName=Wayfarer")
        self.assertIn("", self.driver.title)
    def test_website_Aviator(self):
        self.driver.get("https://theviewoptique.com/Products.aspx?StyleName=Aviator")
        self.assertIn("", self.driver.title)

    def test_products(self):
        self.driver.get("https://theviewoptique.com/Products.aspx?")
        self.driver.find_element("Featured-Categories")
        self.assertIn("Featured-Categories")

    def test_categories(self):
        self.driver.get("https://theviewoptique.com/Products.aspx?GlassesType=Eyeglasses&Gender=Men")
        self.driver.find_element("Men")
        self.assertIn("Men")

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
