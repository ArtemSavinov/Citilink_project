from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    delivery_select = "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/button[2]"
    street = "//input[@placeholder='Введите улицу']"
    house = "//input[@name='house']"
    building = "//input[@name='building']"
    porch = "//input[@name='porch']"
    floor = "//input[@name='floor']"
    flat = "//input[@name='flat']"
    main_price_checkout = "//*[@id='app-check-out']/div/div/div/div[2]/aside/div[3]/div[2]/span/text()"
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

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_select)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house)))

    def get_building(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.building)))

    def get_porch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.porch)))

    def get_floor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.floor)))

    def get_flat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.flat)))

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
        print("Input number")

    def select_delivery(self):
        self.driver.execute_script("window.scrollTo(0, 840)")
        self.get_delivery().click()
        print("Select delivery place")

    def input_street(self, street):
        self.get_street().send_keys(street)
        print("Input street")

    def input_house(self, house):
        self.get_house().send_keys(house)
        print("Input house")

    def input_building(self, building):
        self.get_building().send_keys(building)
        print("Input building")

    def input_porch(self, porch):
        self.get_porch().send_keys(porch)
        print("Input porch")

    def input_floor(self, floor):
        self.get_floor().send_keys(floor)
        print("Input floor")

    def input_flat(self, flat):
        self.driver.execute_script("window.scrollTo(0, 1840)")
        self.get_flat().send_keys(flat)
        print("Input flat")

    def click_paymet_button(self):
        self.driver.execute_script("window.scrollTo(0, 2840)")
        self.get_payment_button().click()
        print("Click payment button")

    # Methods

    def checkout (self):
        self.get_current_url()
        self.input_first_name("Иван")
        self.input_last_name("Иванов")
        self.input_number_phone("9990001122")
        self.assert_word(self.get_main_word_checkout(), 'Компьютер MSI Codex 5 11SI-465XRU, черный')
        self.select_delivery()
        self.input_street("Мира ул.")
        self.input_house("2")
        self.input_building("1")
        self.input_porch("1")
        self.input_floor("16")
        self.input_flat("72")
        self.assert_price(self.get_main_price_checkout(), '96990')
        self.get_screenshot()
        self.click_paymet_button()
