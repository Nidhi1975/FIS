from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_driver():
    """
    Setup and return a configured Chrome WebDriver

    Returns:
        WebDriver: Configured Chrome WebDriver
    """
    chrome_options = Options()
    # Uncomment below for headless mode if needed
    # chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver