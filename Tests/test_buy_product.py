from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.filters_page import Filters_page
from Pages.checkout_page import Checkout_page
from Pages.order_page import Order_page
from Pages.subcategory_page import Subcategory_page
from Pages.main_page import Main_page


def test_buy_product(set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path='C:\\Users\\PRO\\PycharmProjects\\resourse\\chromedriver.exe', chrome_options=options)

    print("Start Test")

    """Выбор категории товара"""

    mp = Main_page(driver)
    mp.select_catalog()

    """Выбор подкатегории товара"""

    pp = Subcategory_page(driver)
    pp.select_subcategory()

    """Выбор товара по параметрам"""

    fp = Filters_page(driver)
    fp.select_filters()

    """Переход на страницу оформления товара"""

    op = Order_page(driver)
    op.registration()

    """Оформление выбраного товара"""

    cp = Checkout_page(driver)
    cp.checkout()

    print("Finish Test")
    driver.quit()



