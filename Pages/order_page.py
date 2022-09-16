from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.base_class import Base


class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart = "//*[@id='content']/div/div/div[1]/div[2]/aside/aside/div[4]/form/button"

    # Getteres

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_cart(self):
        self.get_cart().click()
        print("Go to checkout page")

    # Methods

    def registration (self):
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/order/')
        self.get_screenshot()
        self.click_cart()
