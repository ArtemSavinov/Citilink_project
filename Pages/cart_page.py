import time

import driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart = "//*[@id='content']/div/div/div[1]/div[2]/aside/aside/div[4]/form/button"
    main_price_cart = "//*[@id='content']/div/div/div[1]/div[2]/aside/aside/div[4]/div[1]/span"

    # Getteres

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_main_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_price_cart)))

    # Actions

    def click_cart(self):
        self.get_cart().click()
        print("Click subcategory")

    # Methods

    def registration (self):
        self.get_current_url()
        self.assert_price(self.get_main_price_cart(), '96990')
        self.get_screenshot()
        self.click_cart()
