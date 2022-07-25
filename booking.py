import constants as const
import os
from selenium.webdriver.common.by import By
from booking_filtrations import BookingFiltration
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=const.DRIVER, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency):
        currency_element = self.find_element(By.XPATH, '//button[@data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.find_element(
            By.XPATH,
            f'//a[@data-modal-header-async-url-param="changed_currency=1&selected_currency={currency}&top_currency=1"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.XPATH, '//input[@id="ss"]')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.XPATH, '//li[@data-i="0"]')
        first_result.click()

    def select_date(self, check_in_date, check_out_date, x):
        next_btn_element = self.find_element(By.XPATH, '//div[@data-bui-ref="calendar-next"]')
        for i in range(x):
            next_btn_element.click()

        check_in_element = self.find_element(By.XPATH, f'//td[@data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.XPATH, f'//td[@data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adult(self, count=1):
        selection_element = self.find_element(By.XPATH, '//label[@id="xp__guests__toggle"]')
        selection_element.click()

        while True:
            decrease_adult_element = self.find_element(By.XPATH, '//button[@aria-label="Decrease number of Adults"]')
            decrease_adult_element.click()

            # If the value of adults reaches 1, then we should get out of the while loop
            adults_value_element = self.find_element(By.XPATH, '//input[@id="group_adults"]')
            adults_value = adults_value_element.get_attribute('value')  # Should give back the adults count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(By.XPATH, '//button[@aria-label="Increase number of Adults"]')
        for i in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.XPATH, '//button[@type="submit" and @class="sb-searchbox__button "]')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        try:
            filtration.apply_start_rating(1, 3, 5)
        except Exception as e:
            if 'loading status' in str(e):
                print('Errors in the "apply_start_rating" function\n---> "Error: cannot determine loading status"')
            else:
                raise
        try:
            filtration.sorting()
        except Exception as e:
            if 'Unable to locate element' in str(e):
                print('Errors in the "sorting" function\n---> "No such element: Unable to locate element"')
            else:
                raise
