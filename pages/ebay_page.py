from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EbayPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, 'gh-ac')
        self.search_button = (By.ID, 'gh-btn')
        self.first_item = (By.CSS_SELECTOR, '.srp-results .s-item')
        self.add_to_cart_button = (By.ID, 'add-to-cart-button')
        self.cart_count = (By.CSS_SELECTOR, '.gh-cart-count')

    def navigate_to_ebay(self):
        """Navigate to eBay homepage"""
        self.driver.get('https://www.ebay.com')

    def search_item(self, search_term):
        """Search for an item"""
        search_field = self.driver.find_element(*self.search_input)
        search_field.clear()
        search_field.send_keys(search_term)
        self.driver.find_element(*self.search_button).click()

    def select_first_item(self):
        """Select the first item in search results"""
        first_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_item)
        )
        first_item.click()

    def add_to_cart(self):
        """Add item to cart"""
        add_to_cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_to_cart.click()

    def get_cart_count(self):
        """Get the number of items in cart"""
        cart_count_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cart_count)
        )
        return int(cart_count_element.text)