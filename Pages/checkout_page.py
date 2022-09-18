import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from Base.base_class import Base


class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@name='firstName']"
    last_name = "//input[@name='lastName']"
    number_phone = "//input[@name='phone']"
    paymet_button = "//*[@id='app-check-out']/div/div/div/div[1]/div[4]/div/div[2]/div/div/div[7]/div[3]/div/button"
    delivery_point = "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[3]/button/span"
    select_shop = "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div[2]/button[1]"
    main_word_checkout = "//*[@id='app-check-out']/div/div/div/div[2]/aside/div[2]/div/div/div/div/div/div/div/div/div/div[1]"

    # Getteres

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_number_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_phone)))

    def get_payment_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.paymet_button)))

    def get_delivery_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_point)))

    def get_select_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_shop)))

    def get_main_price_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_price_checkout)))

    def get_main_word_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_checkout)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_number_phone(self, number):
        self.get_number_phone().send_keys(number)
        self.driver.execute_script("window.scrollTo(0, 640)")
        print("Input number")

    def click_delivery_point_button(self):
        self.get_delivery_point().click()
        print("Select delivery point")

    def select_delivery_shop_point(self):
        self.get_select_shop().click()
        print("Select delivery shop")

    def page_down(self):
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 1340)")

    def click_paymet_button(self):
        self.get_payment_button()
        print("Click payment button")

    # Methods

    def checkout (self):
        self.get_current_url()
        self.input_first_name("Иван")
        self.input_last_name("Иванов")
        self.input_number_phone("9990001122")
        self.assert_word(self.get_main_word_checkout(), 'Компьютер MSI Codex 5 11SI-465XRU, черный')
        self.click_delivery_point_button()
        self.select_delivery_shop_point()
        self.page_down()
        self.get_screenshot()
        self.click_paymet_button()


