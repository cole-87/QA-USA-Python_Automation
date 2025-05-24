import time

from selenium.webdriver import Keys

import data
import helpers
from selenium import webdriver

from data import PHONE_NUMBER, CARD_NUMBER

webdriver.Chrome()
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    # Testing if server is on
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Creating 8 functions for testing
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(3)
        assert urban_routes_page.get_from() == data.ADDRESS_FROM
        assert urban_routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(3)
        urban_routes_page.click_call_taxi_button()
        time.sleep(3)
        urban_routes_page.click_supportive_plan()
        time.sleep(3)
        assert urban_routes_page.get_current_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(3)
        urban_routes_page.click_call_taxi_button()
        time.sleep(3)
        urban_routes_page.set_phone(data.PHONE_NUMBER)
        time.sleep(3)
        assert urban_routes_page.get_phone() == PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        assert urban_routes_page.get_card() == data.CARD_NUMBER
        assert urban_routes_page.get_code() == data.CARD_CODE

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(3)
        urban_routes_page.click_call_taxi_button()
        time.sleep(3)
        urban_routes_page.enter_comment_for_driver()
        message = data.MESSAGE_FOR_DRIVER
        time.sleep(3)
        assert urban_routes_page.get_message() == message

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        urban_routes_page.click_order_blanket_and_handkerchiefs()
        assert urban_routes_page.get_blanket_slider_switch_status() == True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_plan()
        time.sleep(2)
        urban_routes_page.select_ice_cream()
        time.sleep(2)
        assert urban_routes_page.get_ice_cream_counter() == 2

    def test_car_search_model_appears(self):
       self.driver.get(data.URBAN_ROUTES_URL)
       urban_routes_page = UrbanRoutesPage(self.driver)
       urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
       time.sleep(2)
       urban_routes_page.click_call_taxi_button()
       urban_routes_page.click_supportive_plan()
       urban_routes_page.enter_comment_for_driver()
       urban_routes_page.click_order_taxi_button()
       assert urban_routes_page.order_taxi_popup() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()