from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.remote_connection import LOGGER

driver = webdriver.Chrome()

driver.get("https://app.vwo.com")

email_address_ele = driver.find_element(By.ID,"login-username")
password_ele = driver.find_element(By.NAME,"password")

sign_in_button_ele = driver.find_element(By.ID,"js-login-btn")

email_address_ele.send_keys("93npu2yyb0@esiix.com")
password_ele.send_keys("Wingify@123")

sign_in_button_ele.click()

time.sleep(5)

#verify test run

LOGGER.info("title is "+driver.title)
assert "Dashboard" in driver.title