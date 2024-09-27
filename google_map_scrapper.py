import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GoogleMapsSearcher:
    def __init__(self, chrome_version):
        """Initialize the Chrome driver using undetected_chromedriver with specified version."""
        self.driver = uc.Chrome(version_main=chrome_version)

    def open_google_maps(self):
        """Open Google Maps in the browser."""
        self.driver.get("https://www.google.com/maps")
        time.sleep(5)  # Wait for the page to load

    def search_location(self, location):
        """Search for a location on Google Maps."""
        search_box = self.driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(location)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)  # Wait for the search results to load

    def click_first_result(self):
        """Click on the first result from the search results."""
        time.sleep(10)
        results_container = self.driver.find_element(By.XPATH, '//div[@role="main"]')
        first_result = results_container.find_element(By.XPATH, './/a[contains(@href, "/place/")]')
        first_result.click()
        time.sleep(5)  # Wait for the details to load

    def get_business_info(self):
        address_element = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label*='Address']")
        address = address_element.get_attribute("aria-label").replace("Address: ", "")

        phone_element = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label*='Phone']")
        phone_number = phone_element.get_attribute("aria-label").replace("Phone: ", "")

        hours_element = self.driver.find_element(By.CSS_SELECTOR, "div[aria-label*='Thursday']")
        opening_hours = hours_element.get_attribute("aria-label")


        business_name = self.driver.find_element(By.XPATH, '//h1[@class="DUwDvf lfPIob"]')
        business_name.text

        # website = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label*='Website']")
        # website.get_attribute('href')

    def close_browser(self):
        """Close the browser."""
        self.driver.quit()

if __name__ == "__main__":
    chrome_version = 127
    maps_searcher = GoogleMapsSearcher(chrome_version)
    maps_searcher.open_google_maps()

    maps_searcher.search_location("Amrit Sweets Mohali")
    maps_searcher.click_first_result()
    business_info = maps_searcher.get_business_info()
    print(business_info)
    maps_searcher.close_browser()
