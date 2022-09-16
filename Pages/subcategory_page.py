import time

import driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base

class Subcategory_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    subcategory = "/html/body/div[3]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[2]/a"

    # Getteres

    def get_subcategory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subcategory)))

    # Actions

    def click_subcategory(self):
        self.driver.execute_script("window.scrollTo(0, 240)")
        time.sleep(4)
        self.get_subcategory().click()
        print("Select subcategory")

    # Methods

    def select_subcategory (self):
        self.get_current_url()
        self.click_subcategory()
