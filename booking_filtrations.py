# This file will include a class with instance methods.
# That will be responsible to interact with our website
# After we have some results, to apply filtrations.

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.sorting_button = None
        self.driver = driver

    def apply_start_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.XPATH, '//div[@id="basiclayout"]//div[@data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        # print(len(star_child_elements))

        for star_value in star_values:
            if star_value == 1:
                one_star_element = self.driver.find_element(By.XPATH,
                                                            '//div[@id="basiclayout"]//div[@data-filters-item="class:class=1"]//span[@class="bbdb949247"]')
                one_star_element.click()

            for stars_element in star_child_elements:
                if str(stars_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    stars_element.click()

    def sorting(self):
        sorting_button = self.driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"and@type="button"]')
        sorting_button.click()

        sort_price_lowest_first = self.driver.find_element(By.XPATH, '//button[@data-id="price"and@type="button"]')
        # sort_price_lowest_first = self.driver.find_element(By.XPATH, '//li[@data-id="price"]')
        sort_price_lowest_first.click()



