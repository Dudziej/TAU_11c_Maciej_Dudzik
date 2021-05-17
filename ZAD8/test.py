import threading
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait(driver):
    try:
        element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.ID, "uc-btn-accept-banner"))
        )
        element.click()
    except:
        print("No RODO")


def wait2async(driver):
    thread = threading.Thread(target=wait, args=[driver])
    thread.start()


def open_site():
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    url = "https://www.zalando.pl/"
    driver.maximize_window()
    driver.get(url)
    wait2async(driver)
    return driver


def search(driver, product):
    search_input = driver.find_element_by_name("q")
    search_input.send_keys(product)
    search_input.send_keys(Keys.ENTER)


def product_click(driver):
    driver.find_elements_by_class_name("heWLCX")[0].click()


def basket_add(driver):
    add_to_basket_button = driver.find_element_by_xpath("//button[@aria-label='Dodaj do koszyka']")
    add_to_basket_button.click()


def basket(driver):
    basket_button = driver.find_element_by_xpath("//a[@title='Koszyk']")
    basket_button.click()


def check_basket(driver, product):
    products = driver.find_elements_by_xpath(f"//a[contains(text(), '{product}')]")
    return len(products) > 0


data = ["The North Face", "Kurtka"]


@pytest.mark.parametrize("product", data)
def test_add_to_basket(product):
    driver = open_site()
    search(driver, product)
    product_click(driver)
    basket_add(driver)
    basket(driver)
    assert check_basket(driver, product)
    driver.quit()
