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
from wise_Wheel_POM.Post_Ad.Post_Ad import hover_element

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
print("Login Successful")
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

driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='My listings']").click()
print("Click on My Listings")
time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='checkAll']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='checkAll']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Select: All']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Delete']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Edit']").click()
time.sleep(2)

#=============================================================================================
image_path = r"C:\Users\WISE MARKET\Documents\Download_1.jpg"
upload_input = driver.find_element(By.NAME, "pictures[]")
upload_input.send_keys(image_path)
print("Image Uploaded")
time.sleep(2)

scrollable_div = driver.find_element(By.CLASS_NAME, "fixed-column")
# Scroll to bottom
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
print("Scroll to bottom")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='phone']").clear()
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("3211122334")
time.sleep(2)

# ==================================Milage===============================================
driver.find_element(By.NAME, "mileage").clear()
driver.find_element(By.NAME, "mileage").send_keys("3000")
time.sleep(5)
#=================================Engine Capacity========================================
driver.find_element(By.NAME, "engine_capacity").clear()
driver.find_element(By.NAME, "engine_capacity").send_keys("3000")
print("Test Pass Capacity")
time.sleep(5)
#=========================================================================
dropdown_element = driver.find_element(By.ID, "cf.32")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("4")
print("Seating Capacity ")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.46")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Duplicate")
print("Car Document")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.43")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Attitude Black")
print("Colour")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.40")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Azad Kashmir")
print("Province")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.38")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Manual")
print("Transmission")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.37")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Diesal")
print("Engine Type")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.35")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Local")
print("Assembly")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.33")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("3")
print("NUMBER OF DOORs")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.31")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Dealers")
print("SELLER TYPE ")
time.sleep(3)

dropdown_element = driver.find_element(By.ID, "cf.1")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Mercedes-Benz")
print("MAKE *")
time.sleep(3)

driver.find_element(By.ID, "cf.2").clear()
driver.find_element(By.ID, "cf.2").send_keys("Best One")
print("Model")
time.sleep(5)

#===============================Feature=================================
driver.find_element(By.ID, "cf.3").clear()
driver.find_element(By.ID, "cf.3").send_keys("2000")
print("Year")
time.sleep(5)

driver.find_element(By.ID, "cf.6.309").click()
time.sleep(2)

driver.find_element(By.ID, "cf.6.346").click()
time.sleep(2)

driver.find_element(By.ID, "cf.6.329").click()
time.sleep(2)

driver.find_element(By.ID, "cf.6.300").click()
time.sleep(2)
# =====================================Price=========================================================
driver.find_element(By.NAME, "price").clear()
driver.find_element(By.NAME, "price").send_keys("500000")
print("Price")
time.sleep(5)
# ==========================================Select City=================================================
driver.find_element(By.XPATH, "//div[@id='cityBox']//span[@role='combobox']").click()
time.sleep(2)
print("Click City")
search_input = driver.find_element(By.XPATH, "//span[contains(@class, 'select2-search--dropdown')]//input")
search_input.send_keys("Karachi")
time.sleep(2)
print("Karachi")
wait = WebDriverWait(driver, 20)
first_option = wait.until(EC.visibility_of_element_located(
	(By.CSS_SELECTOR, "ul#select2-cityId-results li.select2-results__option")
))
first_option.click()
print("Select Karachi, Sindh")
# ==================================================Select Area=========================================
driver.find_element(By.XPATH, "//div[@id='areaBox']//span[@role='combobox']").click()
time.sleep(2)
print("Click Area")
search_input = driver.find_element(By.XPATH, "//span[contains(@class, 'select2-search--dropdown')]//input")
search_input.send_keys("Dha")
time.sleep(2)
print("Dha Defence 7")
wait = WebDriverWait(driver, 20)
area_option = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "ul#select2-areaId-results li.select2-results__option")
))
area_option.click()
print("Select Dha Defence 7")
# ========================================Tag OPtion=====================================================

# ========================================Submit Button=====================================================
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='payableFormSubmitButton']")))

driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(1)  # small delay for smooth scroll

try:
	element.click()
	print("Submit button clicked successfully")
except ElementClickInterceptedException:
	print("Click intercepted. Trying JavaScript click...")
	driver.execute_script("arguments[0].click();", element)
	print("Submit button clicked using JavaScript")



