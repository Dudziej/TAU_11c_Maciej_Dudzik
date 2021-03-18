from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver2 = webdriver.Edge(executable_path='C:\msedgedriver.exe')
driver3 = webdriver.Firefox(executable_path='C:\geckodriver.exe')


# https://www.zalando.pl

url = 'https://www.zalando.pl'

#Scenariusz 1:


driver.maximize_window()
driver.get(url)
button_login = driver.find_element_by_class_name('z-navicat-header_navToolItem')
button_login.click()
input_login = driver.find_element_by_id('login.email')
input_login.send_keys("jakisemailniepoprawny@zle.zle")
input_password = driver.find_element_by_id('login.password')
input_password.send_keys('password')
button_check = driver.find_element_by_class_name('z-coast-reef_forgotpassword_unstyled')
button_check.click()
try:
    z = driver.find_element_by_class_name('OEhtt9')
    print("Test1 Element exists")
except NoSuchElementException:
    print('Test1Element does not exist')


#Scenariusz 2:

driver.maximize_window()
driver.get(url)
button_help = driver.find_element_by_name('headerbanner.help.contact')
button_help.click()
try:
    check_newsletter = driver.find_element_by_link_text('email-nx10k')
    print("Test2 Element exists")
except NoSuchElementException:
    print("Test2 Element does not exist")

#Scenariusz 3:

driver.maximize_window()
driver.get(url)
find_it = driver.find_element_by_class_name('z-navicat-header_searchInput')
find_it.send_keys("dhl")
find_it.send_keys(Keys.ENTER)
try:
    count_it = driver.find_element_by_class_name('cat_count-1RzWf')
    print("Test3 Element exists")
except NoSuchElementException:
    print("Test3 Element does not exist")
driver.close()


#https://www.x-kom.pl/

url2 = 'https://www.x-kom.pl/'

#Scenariusz 1

driver2.maximize_window()
driver2.get(url2)
input_search = driver2.find_element_by_class_name('sc-1hdf4hr-0')
input_search.send_keys('msa')
button_search = driver2.find_element_by_class_name('sc-15gi9e9-7')
button_search.click()
try:
    p = driver2.find_element_by_class_name('sc-1yu46qn-5')
    print("Test4 Element exists")
except NoSuchElementException:
    print("Test4 Element does not exist")


#Scenariusz 2

driver2.get(url2)
button_login2 = driver2.find_element_by_class_name('sc-13bjpvm-6')
button_login2.click()
input_login2 = driver2.find_element_by_class_name('sc-1k5v2vw-1')
input_login2.send_keys("dobrytenemail@masakra.nie")
input_password2 = driver2.find_element_by_class_name('sc-1akovi1-1')
input_password2.send_keys("niezlehaslo")
button_log = driver2.find_element_by_class_name('sc-6i4pc6-2')
button_log.click()
try:
    l = driver2.find_element_by_class_name('dscwo7-6')
    print("Test5 Element exists -")
except NoSuchElementException:
    print("Test5 Element does not exist")
driver2.close()

#Scenariusz 3

driver3.maximize_window()
driver3.get(url2)
button_open = driver3.find_element_by_class_name('sc-13hctwf-5')
button_open.click()
button_new = driver3.find_element_by_class_name('sc-4wflom-8')
button_new.click()
button_product = driver3.find_element_by_class_name('sc-1h16fat-0')
button_product.click()
try:
    o = driver3.find_element_by_class_name('u7xnnm-4')
    print("Test6 Element exists -")
except NoSuchElementException:
    print("Test6 Element does not exist")
driver3.close()

