import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager  # optional automatic install
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://dev.wisewheels.com.pk/")
time.sleep(2)
driver.maximize_window()

# Hover
hover_element = driver.find_element("xpath", "//*[@id='navbarsDefault']/ul[2]/li[4]/a")
print("Hover")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)


# Select Login Option from Drop_Down List
driver.find_element(By.XPATH,"//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover d-md-block d-sm-none d-none']//a[@class='nav-link'][normalize-space()='Log In']").click()
print("Click on Login In")
time.sleep(2)

driver.find_element(By.NAME, "email").send_keys("Test123@yopmail.com")
driver.find_element(By.NAME, "password").send_keys("Aaasss@22")
driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").click()
time.sleep(3)
print("Login Successful")

hover_element = driver.find_element("xpath", "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover']")
print("Hover For Drop_Down")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='Archived listings']").click()
print("Click on Archived Listings")
time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='checkAll']").click()
time.sleep(2)
print("Check_All")
driver.find_element(By.XPATH, "//input[@id='checkAll']").click()
time.sleep(2)
print("Check_All_Again")
driver.find_element(By.XPATH, "//button[normalize-space()='Select: All']").click()
time.sleep(2)
print("Select All")
driver.find_element(By.XPATH, "//button[normalize-space()='Delete']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
print("Delete")

driver.find_element(By.XPATH, "//input[@id='filter']").send_keys("Twoooo")
time.sleep(2)
print("Search")

driver.find_element(By.XPATH, "//input[@id='filter']").clear()
time.sleep(2)
print("Search Clear")
print("Finished")
driver.quit()
