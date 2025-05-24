from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import CARD_NUMBER
from helpers import retrieve_phone_code
import data

import time

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    CUSTOM_OPTION_LOCATOR =(By.XPATH, '//div[text()="Custom"]')
    ACTIVE_PLAN_LOCATOR = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    PHONE_NUMBER = (By.CLASS_NAME, 'np-text')
    PHONE_NUMBER_INPUT_LOCATOR = (By.ID, 'phone')
    PHONE_NUMBER_NEXT = (By.CSS_SELECTOR, '.full')
    SMS_LOCATOR = (By.ID, 'code')
    CONFIRM_LOCATOR = (By.XPATH, '//button[contains(text(), "Confirm")]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    CARD_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
    ADD_CARD_LOCATOR = (By.ID, 'number')
    CARD_CODE_LOCATOR = (By.CSS_SELECTOR, "#code.card-input")
    LINK_BUTTON_LOCATOR =(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    COMMENT_LOCATOR = (By.ID, 'comment')
    SUPPORTIVE_ICON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]')
    ORDER_REQUIREMENTS_LOCATOR = (By.CLASS_NAME, 'reqs-arrow')
    BLANKET_AND_HANDKERCHIEFS_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    SWITCH_STATUS_LOCATOR = (By.XPATH, '(//input[@type="checkbox"])[2]')
    ADD_ICE_CREAM_LOCATOR = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    ICE_CREAM_BUCKET_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[2]/div/img[2]')
    ICE_CREAM_COUNT_LOCATOR = (By.XPATH, '(//div[@class="counter-value"])[1]')
    ORDER_BUTTON_LOCATOR = (By.XPATH, "//span[@class='smart-button-main']")
    ORDER_POPUP_LOCATOR = (By.CLASS_NAME, 'order-header')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property("value")

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON_LOCATOR).click()

    def click_supportive_plan(self):
        # Click to select Supportive plan
        self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).click()


    def get_current_selected_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_LOCATOR).text

    def set_phone(self, number):
        self.driver.find_element(*self.PHONE_NUMBER).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT_LOCATOR).send_keys(data.PHONE_NUMBER)
        time.sleep(3)
        self.driver.find_element(*self.PHONE_NUMBER_NEXT).click()
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.SMS_LOCATOR).send_keys(code)
        time.sleep(3)
        self.driver.find_element(*self.CONFIRM_LOCATOR).click()

    def get_phone(self):
        return self.driver.find_element(*self.PHONE_NUMBER).text

    def enter_comment_for_driver(self):

        self.driver.find_element(*self.COMMENT_LOCATOR).send_keys(data.MESSAGE_FOR_DRIVER)
        time.sleep(3)

    def get_message(self):
        return self.driver.find_element(*self.COMMENT_LOCATOR).get_property("value")

    def set_card_number(self, card_number):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(card_code)

    def get_card(self):
        return self.driver.find_element(*self.ADD_CARD_LOCATOR).get_property("value")

    def get_code(self):
        return self.driver.find_element(*self.CARD_CODE_LOCATOR).get_property("value")

    def fill_card(self, card_number, card_code):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()
        time.sleep(3)
        self.driver.find_element(*self.CARD_LOCATOR).click()
        time.sleep(2)
        self.driver.find_element(*self.ADD_CARD_LOCATOR).send_keys(data.CARD_NUMBER)
        time.sleep(2)
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(data.CARD_CODE)
        time.sleep(2)
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(Keys.TAB)
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def click_order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_LOCATOR).click()

    def get_blanket_slider_switch_status(self):
        return self.driver.find_element(*self.SWITCH_STATUS_LOCATOR).get_property('checked')

    def get_ice_cream_counter(self):
        return int(self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR).text)

    def click_order_requirements(self):
        self.driver.find_element(*self.ORDER_REQUIREMENTS_LOCATOR).click()

    def select_ice_cream(self):
        self.driver.find_element(*self.ADD_ICE_CREAM_LOCATOR).click()
        self.driver.find_element(*self.ADD_ICE_CREAM_LOCATOR).click()

    def order_taxi_popup(self):
        self.driver.find_element(*self.ORDER_POPUP_LOCATOR)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.ORDER_POPUP_LOCATOR))
        return self.driver.find_element(*self.ORDER_POPUP_LOCATOR).is_displayed()

    def click_order_taxi_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()