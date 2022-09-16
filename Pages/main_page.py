import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

from Base.base_class import Base


class Main_page(Base):

    url = 'https://citilink.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    catalog = "//button[@data-label='Каталог товаров']"
    select_category = "/html/body/div[2]/div[2]/header/div[3]/div/div/div/div/div/menu/div/div[2]/div[2]/div[1]/div[2]/a/span"

    # Getteres

    def get_select_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category)))

    # Actions

    def click_catalog(self):
        self.get_select_catalog().click()
        print("Select Catalog")

    def click_category(self):
        self.get_select_category().click()
        print("Select Category")

    # Methods

    def select_catalog (self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_catalog()
        self.click_category()
