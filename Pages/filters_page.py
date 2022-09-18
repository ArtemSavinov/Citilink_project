import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

from Base.base_class import Base


class Filters_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    price_filter = "//*[@id='app-filter']/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/input[2]"
    brand_filter = "//*[@id='app-filter']/div/div[2]/div[2]/div[1]/div[3]/div[3]/div[6]/div[2]/div/div[1]/div/div/div/div/div/div[9]/div/label/span[2]/span"
    parametr_1 = "//*[@id='app-filter']/div/div[2]/div[2]/div[1]/div[3]/div[3]/div[8]/div[2]/div/div/div/div/div/div/div/div[2]/div/label/span[2]/span"
    parametr_2 = "//*[@id='app-filter']/div/div[2]/div[2]/div[1]/div[3]/div[3]/div[9]/div[2]/div/div/div/div/div/div/div/div[3]/div/label/span[2]/span"
    select_product = "/html/body/div[3]/div[2]/main/section/div[1]/div[1]/div[3]/div[1]/section/div[2]/div/div[2]/div[3]/div/div[2]/button"
    cart_button = "//button[@data-label='Перейти в корзину']"
    main_word = "/html/body/div[3]/div[2]/main/section/div[1]/div[1]/div[3]/div[1]/section/div[2]/div/div[1]/div[3]/div/a"
    # Getteres

    def get_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_brand_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_filter)))

    def get_parametr_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.parametr_1)))

    def get_parametr_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.parametr_2)))

    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def select_price_filter(self, price):
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.get_price_filter().click()
        self.get_price_filter().send_keys(Keys.CONTROL + "A")
        self.get_price_filter().send_keys(Keys.DELETE)
        self.get_price_filter().send_keys(price)
        self.get_price_filter().send_keys(Keys.ENTER)
        print("Input max price filter")

    def select_brand_filter(self):
        self.driver.execute_script("window.scrollTo(0, 1340)")
        self.get_brand_filter().click()
        print("Select brand filter")

    def select_paramet_1(self):
        self.driver.execute_script("window.scrollTo(0, 1840)")
        self.get_parametr_1().click()
        print("Select parametr #1 (Video Card)")

    def select_paramet_2(self):
        self.driver.execute_script("window.scrollTo(0, 2140)")
        self.get_parametr_2().click()
        print("Select parametr #2 (RAM)")

    def select_product_1(self):
        self.driver.execute_script("window.scrollTo(0, 240)")
        time.sleep(3)
        self.get_select_product().click()
        print("Select product")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    # Methods

    def select_filters (self):
        self.get_current_url()
        self.select_price_filter("120000")
        self.select_brand_filter()
        self.select_paramet_1()
        self.select_paramet_2()
        self.select_product_1()
        self.assert_word(self.get_main_word(), 'Компьютер MSI Codex 5 11SI-465XRU, черный')
        self.click_cart_button()
