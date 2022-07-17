# This file will include a class with instance methods.
# That will be responsible to interact with our website
# After we have some results, to apply filtrations.
import collections

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_start_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.XPATH, '//div[@data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.XPATH, '*')

        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
