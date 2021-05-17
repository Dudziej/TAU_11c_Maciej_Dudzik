import threading
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def wait(driver):
    try:
        element = WebDriverWait(driver, 600).until(
            expected_conditions.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        element.click()
    except:
        print("No RODO")


def wait2async(driver):
    thread = threading.Thread(target=wait, args=[driver])
    thread.start()


def open_site():
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    url = "https://www2.hm.com/"
    driver.maximize_window()
    driver.get(url)
    wait2async(driver)
    return driver


def search(driver, product):
    search_input = driver.find_element_by_id("main-search")
    search_input.send_keys(product)
    search_input.send_keys(Keys.ENTER)


def product_click(driver):
    driver.find_elements_by_class_name("image-container")[0].click()


def basket_add(driver):
    driver.find_elements_by_class_name("product-item-buttons")[0].click()
    driver.find_elements_by_class_name("option")[1].click()
    random_element = driver.find_element_by_tag_name("body")
    ActionChains(driver).move_to_element(random_element).perform()
    driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[1]/button").click()


def basket(driver):
    basket_button = driver.find_element_by_xpath("//a[@title='Koszyk']")
    basket_button.click()


def check_basket(driver):
    time.sleep(2)
    shopping_cart = driver.find_element_by_class_name("shoppingbag-item-count").get_attribute("innerHTML")
    return len(shopping_cart) > 0


data = ["Women", "lingerie"]


def language(driver):
    driver.find_element_by_id("link_en_us").click()


@pytest.mark.parametrize("product", data)
def test_add_to_basket(product):
    driver = open_site()
    language(driver)
    search(driver, product)
    product_click(driver)
    basket_add(driver)
    assert check_basket(driver)
    driver.quit()
