import pytest
from utils.web_utils import get_driver
from pages.ebay_page import EbayPage


class TestEbayCart:
    @pytest.fixture(scope='function')
    def driver(self):
        """Setup WebDriver for each test"""
        driver = get_driver()
        yield driver
        driver.quit()

    def test_add_item_to_cart(self, driver):
        """
        Test adding a book to cart on eBay

        Steps:
        1. Navigate to eBay
        2. Search for 'book'
        3. Select first book
        4. Add to cart
        5. Verify cart count
        """
        ebay_page = EbayPage(driver)

        # Navigate and search
        ebay_page.navigate_to_ebay()
        ebay_page.search_item('book')
        ebay_page.select_first_item()

        # Add to cart
        ebay_page.add_to_cart()

        # Verify cart count
        cart_count = ebay_page.get_cart_count()
        assert cart_count > 0, "Cart should have at least one item"