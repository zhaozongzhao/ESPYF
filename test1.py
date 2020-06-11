import time

from selenium import webdriver
from PYFUI import login_elenium

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\user\AppData\Local\Programs\erp-client\派药房.exe"
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=r'C:\Users\user\AppData\Local\Google\Chrome\Application\chromedriver.exe'
                          , port=9515)

driver.find_element_by_xpath(login_elenium.user).send_keys('')
time.sleep(3)
driver.find_element_by_xpath(login_elenium.password).send_keys('')
time.sleep(3)
driver.find_element_by_xpath(login_elenium.button).click()
time.sleep(10)
driver.quit()
