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
#===============================================Pending Approvel===============================================
driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='Pending approval']").click()
print("Pending Approval")
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
driver.back()
time.sleep(2)
print("Back From Pending Approval")
#========================================Favrouite Listing==============================================================

hover_element = driver.find_element("xpath", "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover']")
print("Hover For Drop_Down")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='Favourite listings']").click()
print("Pending Approval")
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
driver.find_element(By.XPATH, "//input[@id='filter']").send_keys("Twoooo")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='filter']").clear()
time.sleep(2)
driver.back()
time.sleep(2)
print("Back From Favourite Listings")
#===================================Messages====================================================
hover_element = driver.find_element("xpath", "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover']")
print("Hover For Drop_Down")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='Messenger']").click()
print("Click on Messengers")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='form-check-all']").click()
time.sleep(2)
print("Click All")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropdown-toggle')]//span[text()='Action']"))
).click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Mark as read']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
print("Mark as read")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropdown-toggle')]//span[text()='Action']"))
).click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Mark as unread']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
print("Mark as unread")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropdown-toggle')]//span[text()='Action']"))
).click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Mark as Important']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
print("Mark as Important")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropdown-toggle')]//span[text()='Action']"))
).click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Mark as not important']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
print("Mark as not Important")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropdown-toggle')]//span[text()='Action']"))
).click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Delete']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
print("Mark Delete")

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='btnRefresh']"))
).click()
time.sleep(2)
print("click Refresh")

driver.find_element(By.XPATH, "//button[normalize-space()='More']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Mark all as read']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
time.sleep(2)
print("click More Option")

driver.find_element(By.XPATH, "//a[normalize-space()='Unread']").click()
time.sleep(2)
print("Unread")
driver.find_element(By.XPATH, "//a[normalize-space()='Started']").click()
time.sleep(2)
print("Started")
driver.find_element(By.XPATH, "//a[normalize-space()='Important']").click()
time.sleep(2)
print("Important")
driver.back()
time.sleep(2)
print("Back From Messages Screen")
#===========================================Save Searches===================================================
hover_element = driver.find_element("xpath", "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover']")
print("Hover For Drop_Down")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='Saved searches']").click()
print("Save_Searches_Screen")
time.sleep(3)
driver.back()
#========================================My Account=============================================
hover_element = driver.find_element("xpath", "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover']")
print("Hover For Drop_Down")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='My Account']").click()
time.sleep(2)
print("Click on My Account")
# driver.find_element(By.CSS_SELECTOR, "#select2-genderId-container").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#select2-genderId-result-zwu7-1").click()
# time.sleep(2)
image_path = r"C:\Users\WISE MARKET\Documents\Download_1.jpg"
upload_input = driver.find_element(By.XPATH, "//input[@id='photoField']")
upload_input.send_keys(image_path)
print("Image Uploaded")
time.sleep(2)

email_field = driver.find_element(By.XPATH, "//input[@name='name']")
email_field.clear()
email_field.send_keys("Alpha")
time.sleep(2)
print("Name_Alpha")
email_field = driver.find_element(By.XPATH, "//input[@id='username']")
email_field.clear()
email_field.send_keys("Alpha Beta")
time.sleep(2)
print("UserName_Alpha Beta")

# driver.find_element(By.XPATH, "//input[@id='phoneAuthField']").click()
# time.sleep(2)
# print("Click SMS")

email_field = driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='email']")
email_field.clear()
email_field.send_keys("Alpha@Beta.com")
time.sleep(2)
print("Email Enterer")

email_field = driver.find_element(By.XPATH, "//input[@id='phone']")
email_field.clear()
email_field.send_keys("03312233453")
time.sleep(2)
print("Password Enterer")

driver.find_element(By.XPATH, "//input[@id='phoneHidden']").click()
time.sleep(2)
print("Password Hidden")

driver.find_element(By.XPATH, "//form[@name='details']//button[@type='submit'][normalize-space()='Update']").click()
print("Profile Updated")
time.sleep(2)
driver.back()
time.sleep(2)

#============================================Log Out========================================
hover_element = driver.find_element("xpath", "//nav[@role='navigation']//li[@class='nav-item dropdown no-arrow open-on-hover']")
print("Hover For Drop_Down")
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//nav[@role='navigation']//a[normalize-space()='Log Out']").click()
time.sleep(2)
print("Log Out Successful")

