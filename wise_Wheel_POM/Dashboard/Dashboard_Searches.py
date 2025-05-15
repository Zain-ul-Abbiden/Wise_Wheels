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
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Search your favorite car, brand, models']").send_keys("Suzuki")
time.sleep(1)
print("Suzuki")
driver.find_element(By.XPATH, "//input[@id='locSearch']").send_keys("Karachi")
time.sleep(1)
print("Karachi sindh")
wait = WebDriverWait(driver, 10)
first_option = wait.until(EC.visibility_of_element_located(
	(By.CSS_SELECTOR, "#autoComplete_result_0")
))
first_option.click()
print("Selected")
driver.find_element(By.CSS_SELECTOR, ".col-md-12.col-lg-3.mb-2").click()
time.sleep(5)
print("Search Button")

#Select All Categories
driver.find_element(By.XPATH, "//a[@id='toggleCategories']").click()
time.sleep(3)

button = driver.find_element(By.XPATH, "//span[normalize-space()='Electric']")
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
time.sleep(1)
button.click()

print("Categori_Electric")

time.sleep(3)

#Document
dropdown_element = driver.find_element(By.ID, "cf.46")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Duplicate")
print("Car Document")
time.sleep(3)

#Colour
dropdown_element = driver.find_element(By.ID, "cf.43")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Attitude Black")
print("Colour")
time.sleep(3)

#Transmission
dropdown_element = driver.find_element(By.ID, "cf.38")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Manual")
print("Transmission")
time.sleep(3)

#Engine Type
dropdown_element = driver.find_element(By.ID, "cf.37")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Diesal")
print("Engine Type")
time.sleep(3)

#Assembly
dropdown_element = driver.find_element(By.ID, "cf.35")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Local")
print("Assembly")
time.sleep(3)

#Make
dropdown_element = driver.find_element(By.ID, "cf.1")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Mercedes-Benz")
print("MAKE *")
time.sleep(5)

#==================================Feature===========================================
wait = WebDriverWait(driver, 10)
label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='cf.6.300']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
driver.execute_script("arguments[0].click();", label)
print("Click ABS")

wait = WebDriverWait(driver, 10)
label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='cf.6.346']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
driver.execute_script("arguments[0].click();", label)

wait = WebDriverWait(driver, 10)
label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='cf.6.329']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
driver.execute_script("arguments[0].click();", label)

wait = WebDriverWait(driver, 10)
label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='cf.6.313']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
driver.execute_script("arguments[0].click();", label)
print("Feature Done")
time.sleep(3)

driver.find_element(By.NAME, "cf[38]").send_keys("2023")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div[class='col-lg-3 col-md-12 col-sm-12'] button[type='submit']").click()
# print("Year")
time.sleep(10)
#
# driver.find_element(By.XPATH, "//a[@title='Cars']").click()
# time.sleep(5)

#Select Locations
driver.find_element(By.XPATH, "//a[@id='toggleLocations']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Karachi']").click()
time.sleep(5)
print("Karachi")

#Select Area
driver.find_element(By.XPATH, "//a[normalize-space()='Abul Hassan Isphani Road']").click()
time.sleep(3)
print("Area Selected")

#Select Date
driver.find_element(By.XPATH, "//a[@id='toggleDateFilter']").click()
driver.find_element(By.CSS_SELECTOR, "#postedDate_184").click()
print("Date Selected")

#Frpm Year to To Go
driver.find_element(By.ID, "year_from").send_keys("2000")
driver.find_element(By.ID, "year_to").send_keys("2025")
driver.find_element(By.CSS_SELECTOR, "div[class='main-container'] div:nth-child(3) button:nth-child(1)").click()
print("From Year to Too")
